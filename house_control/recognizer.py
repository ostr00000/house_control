from typing import Type

from house_control.device import Device
from house_control.event import MyEvent
from house_control.exceptions import LocationNotFound, DeviceNotFound, EventNotFound
from house_control.location import Loc


class Recognizer:
    def __init__(self, location: Loc, currentLocation: Loc = None):
        self.location = location
        self.currentLocation = currentLocation if currentLocation else location

    def recognise(self, command):
        command = self._baseProcessing(command)
        eventType = self._getEventType(command)
        print(eventType)

        device = self._getDevice(command)
        print(device)

    @staticmethod
    def _baseProcessing(command: str):
        return command.lower()

    def _getEventType(self, command) -> Type:
        verb = self.getBaseVerb(command)
        for subclass in MyEvent.__subclasses__():  # type: Type[MyEvent]
            verbs = subclass.getVerbs()
            if verb in verbs:
                return subclass

        return EventNotFound

    @staticmethod
    def getBaseVerb(command: str):
        """Move verb to base form"""
        return command.split(' ')[0] + 'yć'  # TODO

    def _getDevice(self, command: str) -> Device:
        loc = self.getLocation(command)
        if loc is LocationNotFound:
            device = self.getDeviceIfUnique(command)
        else:
            device = self.getDeviceFromLocation(command, loc)
        return device

    def getLocation(self, command):
        nouns = self.getNouns(command)
        for location in (self.currentLocation, self.location):
            for name in ([location.name] + location.aliases):
                if name in nouns:
                    return location

        return LocationNotFound

    @staticmethod
    def getNouns(command):
        return [
            command.split(' ')[1],
            command.split(' ')[3] + 'a',
        ]

    def getDeviceIfUnique(self, command):
        nouns = self.getNouns(command)
        founded = []

        for location in (self.currentLocation, self.location):
            for device in location.devices:
                for devName in ([device.name] + device.aliases):
                    if devName in nouns:
                        founded.append(device)

        if len(founded) == 1:
            return founded[0]

        return DeviceNotFound(*founded)

    def getDeviceFromLocation(self, command: str, loc: Loc):
        nouns = self.getNouns(command)

        for device in loc.devices:
            for name in ([device.name] + device.aliases):
                if name in nouns:
                    return device

        if len(loc.devices) == 1:
            return DeviceNotFound(loc.devices[0])

        return DeviceNotFound()
