from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class BrightnessEvent(BaseHouseEvent):
    aliases = AliasSet('jasność')

    def __str__(self):
        return f'set {self.device} bright {self.getBrightness()}'

    def getBrightness(self):
        pass
