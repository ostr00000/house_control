from house_control.event import BaseHouseEvent


class BrightnessEvent(BaseHouseEvent):
    aliases = {'jasność'}

    def __repr__(self):
        return 'set <DEV> bright <N>'
