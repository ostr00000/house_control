from house_control.event import BaseHouseEvent


class VerticalEvent(BaseHouseEvent):
    aliases = {'dół', 'góra', 'stop'}

    def __repr__(self):
        return 'up <DEV>'
        return 'down <DEV>'
        return 'stop <DEV>'
