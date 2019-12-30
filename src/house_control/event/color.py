from house_control.event import BaseHouseEvent


class ColorEvent(BaseHouseEvent):
    aliases = {'ciepły', 'zimny'}

    def __repr__(self):
        return 'cold <DEV>'
        return 'warm <DEV>'
