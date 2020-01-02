from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class TimeEvent(BaseHouseEvent):
    aliases = AliasSet('ustaw')

    def __str__(self):
        return 'set <DEV> time <gg:mm>'
