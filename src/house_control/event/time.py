from house_control.event import BaseHouseEvent


class TimeEvent(BaseHouseEvent):
    aliases = {'ustaw'}

    def __repr__(self):
        return 'set <DEV> time <gg:mm>'
