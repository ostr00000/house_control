from house_control.event import BaseHouseEvent


class SpeedEvent(BaseHouseEvent):
    aliases = {'szybciej', 'wolniej'}

    def __repr__(self):
        return 'fast <DEV>'
        return 'slow <DEV>'
