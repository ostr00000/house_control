from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet


class VerticalEvent(BaseHouseEvent):
    aliases = AliasSet('dół', 'góra', 'stop')

    def __str__(self):
        if self.isUp():
            action = 'up'
        elif self.isDown():
            action = 'down'
        else:
            action = 'stop'

        return f"{action} {self.device}"

    def isUp(self):
        pass

    def isDown(self):
        pass
