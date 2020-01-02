from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class BrightnessEvent(BaseHouseEvent):
    aliases = AliasSet('jasność')

    def __repr__(self):
        return 'set <DEV> bright <N>'
