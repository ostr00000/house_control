from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class SpeedEvent(BaseHouseEvent):
    aliases = AliasSet('szybciej', 'wolniej')

    def __str__(self):
        return f"{'fast' if self.isFast() else 'slow'} {self.device}"

    def isFast(self):
        pass
