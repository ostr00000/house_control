from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class VerticalEvent(BaseHouseEvent):
    aliases = AliasSet('dół', 'góra', 'stop')

    def __repr__(self):
        return 'up <DEV>'
        return 'down <DEV>'
        return 'stop <DEV>'
