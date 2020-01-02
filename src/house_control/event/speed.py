from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class SpeedEvent(BaseHouseEvent):
    aliases = AliasSet('szybciej', 'wolniej')

    def __str__(self):
        return 'fast <DEV>'
        return 'slow <DEV>'
