from __future__ import annotations

import logging
from itertools import chain
from typing import Optional, Type, Dict, Iterable, TypeVar, List

from house_control.event import BaseHouseEvent
from house_control.exceptions import UnknownAction, UnknownDevice
from house_control.model.command import Command
from house_control.model.device import Device
from house_control.model.location import Loc

logger = logging.getLogger(__name__)
T = TypeVar('T')


def multiMax(*iterable: Iterable[T], key=None) -> List[T]:
    maxKey = max(*iterable, key=key)
    maxVal = key(maxKey)
    key = key if key else lambda x: x
    return list(set(i for it in iterable for i in it if key(i) == maxVal))


class HouseEventBuilder:
    def __init__(self, command: Command):
        self.command = command

        self.typeCandidates: Dict[Type[BaseHouseEvent], int] = {}
        self.deviceCandidates: Dict[Device, int] = {}
        self.locationCandidates: Dict[Loc, int] = {}
        self.currentLocation: Optional[Loc] = None

    def findType(self):
        for subclass in BaseHouseEvent.__subclasses__():  # type: Type[BaseHouseEvent]
            intersected = self.command.set.intersection(subclass.aliases)
            if intersected:
                self.typeCandidates[subclass] = len(intersected)

        return self

    def findLocation(self, location: Loc):
        for loc in location:
            intersected = self.command.set.intersection(loc.aliases)
            if intersected:
                self.locationCandidates[loc] = len(intersected)

        return self

    def setCurrentLocation(self, currentLocation: Loc):
        self.currentLocation = currentLocation
        return self

    def findDevice(self) -> HouseEventBuilder:
        cur = self.currentLocation if self.currentLocation else {}
        self.deviceCandidatesDebug = {}  # DEBUG

        mostPossibleLoc = set(self.locationCandidates.keys())
        mostPossibleLoc.update(iter(cur))
        for loc in mostPossibleLoc:
            deep = loc.deep()
            isInCurLocation = loc in cur
            possibleLocation = self.locationCandidates.get(loc, 0)

            for device in loc.devices:
                command = self.command.set.difference(loc.aliases)
                intersected = command.intersection(device.aliases)
                requirementMeet = device.isRequirementMeet(cmd=self.command)
                if intersected:
                    val = (
                            + 1 * deep
                            + 10 * isInCurLocation
                            + 100 * possibleLocation
                            + 1000 * len(intersected)
                            + 10000 * requirementMeet
                    )
                    self.deviceCandidates[device] = val
                    self.deviceCandidatesDebug[device] = intersected

        return self

    def build(self) -> BaseHouseEvent:
        classObject = self.extractType()
        device = self.extractDevice(classObject)
        return classObject(device, self.command)

    def extractType(self) -> Type[BaseHouseEvent]:
        if self.typeCandidates:
            possibleTypes = set(chain(*(dev.actions for dev in self.deviceCandidates.keys())))
            validTypeCandidates = {tc: val for tc, val in self.typeCandidates.items()
                                   if tc in possibleTypes}
            if validTypeCandidates:
                if len(validTypeCandidates) == 1:
                    return next(iter(validTypeCandidates.keys()))
                best = max(validTypeCandidates, key=validTypeCandidates.get)
            else:
                best = max(self.typeCandidates, key=self.typeCandidates.get)
            return best

        dev = self.extractDevice()
        if dev.defaultAction:
            return dev.defaultAction

        raise UnknownAction(device=dev)

    def extractDevice(self, eventType: Type[BaseHouseEvent] = None) -> Device:
        if self.deviceCandidates:
            dev = {k: v for k, v in self.deviceCandidates.items() if eventType in k.actions}
            if not dev:
                dev = self.deviceCandidates

            if len(dev) == 1:
                return list(self.deviceCandidates.keys())[0]

            maxValues = multiMax(self.deviceCandidates, key=self.deviceCandidates.get)
            if len(maxValues) == 1:
                return maxValues[0]

            filtered = list(filter(lambda x: x.aggr is not None, maxValues))  # DEBUG
            if any((aggr := m) for m in maxValues if m.aggr):
                return aggr

            return maxValues[0]

        if len(self.locationCandidates) == 1:
            loc = next(iter(self.locationCandidates))
            if len(loc.devices) == 1:
                return loc.devices[0]

            devices = [dev for dev in loc.devices if eventType in dev.actions]
            if len(devices) == 1:
                return devices[0]

        # TODO add all house for device with unique action

        raise UnknownDevice
