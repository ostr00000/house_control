from __future__ import annotations

from itertools import chain
from typing import Optional, Type, Dict, Iterable, TypeVar, List

from house_control.event import BaseHouseEvent
from house_control.exceptions import UnknownAction, UnknownDevice
from house_control.model.command import Command
from house_control.model.device import Device
from house_control.model.location import Loc

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
        for loc in chain(self.locationCandidates.keys(), (self.currentLocation,)):
            for device in loc.devices:
                intersected = self.command.set.intersection(device.aliases)
                if intersected:
                    factor = 100 if loc == self.currentLocation else 0
                    self.deviceCandidates[device] = len(intersected) + factor

        return self

    def build(self) -> BaseHouseEvent:
        classObject = self.extractType()
        device = self.extractDevice(classObject)
        return classObject(device, self.command)

    def extractType(self) -> Type[BaseHouseEvent]:
        if self.typeCandidates:
            return max(self.typeCandidates, key=self.typeCandidates.get)

        dev = None
        if len(self.deviceCandidates) == 1:
            dev = next(iter(self.deviceCandidates))

        elif len(self.locationCandidates) == 1:
            loc = next(iter(self.locationCandidates))
            if len(loc.devices) == 1:
                dev = loc.devices[0]

        if dev and dev.defaultAction:
            return dev.defaultAction

        raise UnknownAction

    def extractDevice(self, eventType: Type[BaseHouseEvent]) -> Device:
        if self.deviceCandidates:
            dev = {k: v for k, v in self.deviceCandidates.items() if eventType in k.actions}
            if not dev:
                dev = self.deviceCandidates

            if len(dev) == 1:
                return list(self.deviceCandidates.keys())[0]

            maxValues = multiMax(self.deviceCandidates, key=self.deviceCandidates.get)
            if len(maxValues) == 1:
                return maxValues[0]

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
