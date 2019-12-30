from house_control.event import BaseHouseEvent


class ChannelEvent(BaseHouseEvent):
    aliases = {'kanał', 'poprzedni', 'następny'}

    def __repr__(self):
        return 'set <DEV> ch <N>'
        return 'ch_next <DEV>'
        return 'ch_prev <DEV>'
