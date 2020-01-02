from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class VolumeEvent(BaseHouseEvent):
    aliases = AliasSet('głośniej', 'ciszej', 'podgłośnić', 'ściszyć')

    def __repr__(self):
        return 'set <DEV> vol <N>'
        return 'vol_up <N>'
        return 'vol_down <N>'
