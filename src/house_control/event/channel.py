from typing import Optional

from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet
from house_control.model.numbers import findNumber


class ChannelEvent(BaseHouseEvent):
    aliases = AliasSet('kanał', 'poprzedni', 'następny')

    def __str__(self):
        channel = self.getChannel()
        if channel is not None:
            return f'set {self.device} ch {channel}'

        return f"{'ch_next' if self.isNext() else 'ch_prev'} {self.device}"

    def getChannel(self) -> Optional[int]:
        return findNumber(self.command.sequence)

    def isNext(self):
        pass
