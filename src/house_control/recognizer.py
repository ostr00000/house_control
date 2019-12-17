from typing import Union

from house_control.event import BaseHouseEvent
from house_control.event.builder import HouseEventBuilder
from house_control.model.command import Command
from house_control.model.location import Loc
from house_control.process_language import baseProcessing


class Recognizer:
    def __init__(self, location: Loc, currentLocation: Loc = None):
        self.location = location
        self.currentLocation = currentLocation if currentLocation else location

    def getTextFromSpeak(self):
        """Send speak to external service"""
        raise NotImplementedError

    def recognizeEvent(self, command: Union[str, Command]) -> BaseHouseEvent:
        if not isinstance(command, Command):
            if isinstance(command, str):
                command = Command(command)
            else:
                raise ValueError(f'Invalid argument type "{type(command)}" for command')

        builder = HouseEventBuilder(command)
        builder.findType()
        builder.findLocation(self.location)
        builder.setCurrentLocation(self.currentLocation)
        builder.findDevice()

        return builder.build()
