from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class ChannelEvent(BaseHouseEvent):
    aliases = AliasSet('kanał', 'poprzedni', 'następny')

    def __str__(self):
        return 'set <DEV> ch <N>'
        return 'ch_next <DEV>'
        return 'ch_prev <DEV>'
