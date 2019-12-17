from __future__ import annotations

from itertools import chain
from typing import Optional, Type, Dict, TypeVar

from house_control.event import BaseHouseEvent
from house_control.exceptions import UnknownAction, UnknownDevice
from house_control.model.command import Command
from house_control.model.device import Device
from house_control.model.location import Loc

T = TypeVar('T')


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
                    self.deviceCandidates[device] = len(intersected)

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
            return max(self.deviceCandidates, key=self.deviceCandidates.get)

        if len(self.locationCandidates) == 1:
            loc = next(iter(self.locationCandidates))
            if len(loc.devices) == 1:
                return loc.devices[0]

            devices = [dev for dev in loc.devices if eventType in dev.actions]
            if len(devices) == 1:
                return devices[0]

        # TODO add all house for device with unique action

        raise UnknownDevice
