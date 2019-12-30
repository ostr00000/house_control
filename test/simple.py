from house_control.event.switch import SwitchEvent
from house_control.house_configuration import house, kitchen
from house_control.recognizer import Recognizer


def test_simple():
    rec = Recognizer(house)
    cmd = 'włącz światło w kuchni'
    event = rec.recognizeEvent(cmd)
    assert isinstance(event, SwitchEvent)
    assert event.device.loc is kitchen
    assert str(event.command) == cmd
