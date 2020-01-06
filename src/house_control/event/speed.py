from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet
from house_control.exceptions import UnknownAction


class SpeedEvent(BaseHouseEvent):
    actionMap = {
        ('szybko', 'szybciej'): 'fast',
        ('wolno', 'wolniej'): 'slow',
    }
    aliases = AliasSet(*actionMap.keys())

    def __str__(self):
        for i, action in enumerate(self.actionMap.values()):
            if self.isInGroup(i):
                return f"{action} {self.device}"

        raise UnknownAction(f"Cannot recognize speed: {self.command.sequence}")
