from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class ColorEvent(BaseHouseEvent):
    aliases = AliasSet('ciepły', 'zimny')

    def __str__(self):
        return f"{'warm' if self.isWarm() else 'cold'} {self.device}"

    def isWarm(self):
        pass
