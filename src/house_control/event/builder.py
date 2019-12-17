from typing import Optional, List, Type

from house_control.event import BaseHouseEvent
from house_control.model import Loc
from house_control.model.command import Command

Candidate = Type[BaseHouseEvent]


class HouseEventBuilder:
    def __init__(self):
        self.typeCandidates: List[Candidate] = []
        self.deviceCandidates: List[Candidate] = []

        self.currentLocation: Optional[Loc] = None

    def findType(self, command: Command):
        for subclass in BaseHouseEvent.__subclasses__():  # type: Type[BaseHouseEvent]
            if command.set.intersection(subclass.aliases):
                self.deviceCandidates.append(subclass)

        return self

    def findLocation(self, command: Command, location: Loc):
        return self  # TODO

    def setCurrentLocation(self, currentLocation: Loc):
        self.currentLocation = currentLocation
        return self

    def findDevice(self, command) -> 'HouseEventBuilder':
        return self  # TODO

    def build(self) -> BaseHouseEvent:
        pass  # TODO choose best result
