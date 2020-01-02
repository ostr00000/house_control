from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class ToggleEvent(BaseHouseEvent):
    aliases = AliasSet('przełącz')

    def __repr__(self):
        return 'toggle'
