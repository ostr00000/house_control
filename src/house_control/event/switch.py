from house_control.event import BaseHouseEvent


class SwitchEvent(BaseHouseEvent):
    aliases = {'włącz', 'wyłącz'}

    def __repr__(self):
        return 'toggle'



