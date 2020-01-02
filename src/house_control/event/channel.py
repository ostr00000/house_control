from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class ChannelEvent(BaseHouseEvent):
    aliases = AliasSet('kanał', 'poprzedni', 'następny')

    def __str__(self):
        channel = self.getChannel()
        if channel:
            return f'set {self.device} ch {channel}'

        return f"{'ch_next' if self.isNext() else 'ch_prev'} {self.device}"

    def getChannel(self) -> int:
        pass

    def isNext(self):
        pass
