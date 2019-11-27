class MyEvent:
    @classmethod
    def getVerbs(cls):
        raise NotImplementedError


class SwitchEvent(MyEvent):
    @classmethod
    def getVerbs(cls):
        return ['włączyć', 'wyłączyć', 'zaświecić', 'zgasić']

    def __init__(self, active=True, toggle=False):
        self.active = active
        self.toggle = toggle
