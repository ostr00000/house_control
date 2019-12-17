from house_control.event import BaseHouseEvent


class SwitchEvent(BaseHouseEvent):
    alias = ['włączyć', 'wyłączyć', 'zaświecić', 'zgasić']

    def __init__(self, active=True, toggle=False):
        self.active = active
        self.toggle = toggle

