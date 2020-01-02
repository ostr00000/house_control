from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class ColorEvent(BaseHouseEvent):
    aliases = AliasSet('ciepły', 'zimny')

    def __str__(self):
        return 'cold <DEV>'
        return 'warm <DEV>'
