from house_control.event import BaseHouseEvent


class ToggleEvent(BaseHouseEvent):
    aliases = {'przełącz'}

    def __repr__(self):
        return 'toggle'
