from typing import Type

from house_control.device import Device
from house_control.event import MyEvent
from house_control.exceptions import LocationNotFound, DeviceNotFound, EventNotFound
from house_control.location import Loc
from house_control.process_language import baseProcessing, getBaseVerb, getNouns


class Recognizer:
    def __init__(self, location: Loc, currentLocation: Loc = None):
        self.location = location
        self.currentLocation = currentLocation if currentLocation else location

    def recognise(self, command):
        command = baseProcessing(command)
        eventType = self._getEventType(command)
        print(eventType)

        device = self._getDevice(command)
        print(device)

    def _getEventType(self, command) -> Type:
        verb = getBaseVerb(command)
        for subclass in MyEvent.__subclasses__():  # type: Type[MyEvent]
            verbs = subclass.getVerbs()
            if verb in verbs:
                return subclass

        return EventNotFound

    def _getDevice(self, command: str) -> Device:
        loc = self.getLocation(command)
        if loc is LocationNotFound:
            device = self.getDeviceIfUnique(command)
        else:
            device = self.getDeviceFromLocation(command, loc)
        return device

    def getLocation(self, command):
        nouns = getNouns(command)
        for location in (self.currentLocation, self.location):
            for name in ([location.name] + location.aliases):
                if name in nouns:
                    return location

        return LocationNotFound

    def getDeviceIfUnique(self, command):
        nouns = getNouns(command)
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
        nouns = getNouns(command)

        for device in loc.devices:
            for name in ([device.name] + device.aliases):
                if name in nouns:
                    return device

        if len(loc.devices) == 1:
            return DeviceNotFound(loc.devices[0])

        return DeviceNotFound()
