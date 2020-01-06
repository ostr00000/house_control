from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet
from house_control.exceptions import UnknownAction
from house_control.model.numbers import findNumber


class BrightnessEvent(BaseHouseEvent):
    aliases = AliasSet('jasność', 'ustaw', '%')

    def __str__(self):
        if number := findNumber(self.command.sequence):
            return f'set {self.device} bright {number}'

        raise UnknownAction(f"Cannot find brightness level '{self.command.sequence}'")
