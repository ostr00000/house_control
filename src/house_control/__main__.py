import logging

from house_control.model.device import Device
from house_control.event import SwitchEvent
from house_control.model.location import Loc
from house_control.recognizer import Recognizer


def main():
    dom = Loc('dom', {'mieszkanie'})
    k = Loc('kuchnia', parent=dom)
    lam = Device('lampa', k, {'światło'}, [SwitchEvent])

    recognizer = Recognizer(dom, currentLocation=k)
    event = recognizer.recognizeEvent("WŁĄCZ światlo w kuchni")
    print(event)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
