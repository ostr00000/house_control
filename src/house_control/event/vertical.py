from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet
from house_control.exceptions import UnknownAction


class VerticalEvent(BaseHouseEvent):
    actionMap = {
        ('dół', 'opuść', 'zasłoń'): 'down',
        ('góra', 'podnieś', 'odsłoń'): 'up',
        ('stop', 'zatrzymaj'): 'stop',
    }
    aliases = AliasSet(*tuple(actionMap.keys()))

    def __str__(self):
        for i, action in enumerate(self.actionMap.values()):
            if self.isInGroup(i):
                return f"{action} {self.device}"

        raise UnknownAction(f"Cannot recognize action: {self.command.sequence}")
