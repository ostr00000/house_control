from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class VolumeEvent(BaseHouseEvent):
    aliases = AliasSet('głośniej', 'ciszej', 'pogłośnić', 'ściszyć')

    def __str__(self):
        vol = self.getVolume()
        if vol:
            return f"set {self.device} vol {vol}"

        return f"{'vol_up' if self.isVolumeUp() else 'vol_down'} {self.device}"

    def getVolume(self) -> int:
        pass

    def isVolumeUp(self):
        pass
