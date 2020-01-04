from typing import Optional

from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet
from house_control.model.numbers import findNumber


class VolumeEvent(BaseHouseEvent):
    aliases = AliasSet('ustaw', ('głośniej', 'pogłośnić',), ('ciszej', 'ściszyć'))

    def __str__(self):
        vol = self.getVolume()
        if vol is not None:
            return f"set {self.device} vol {vol}"

        return f"{'vol_up' if self.isInGroup(1) else 'vol_down'} {self.device}"

    def getVolume(self) -> Optional[int]:
        return findNumber(self.command.sequence)
