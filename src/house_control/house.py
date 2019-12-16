from house_control.device import Device
from house_control.event import SwitchEvent
from house_control.location import Loc
from house_control.recognizer import Recognizer


def main():
    dom = Loc('dom', ['mieszkanie'])
    k = Loc('kuchnia', parent=dom)
    lam = Device('lampa', k, ['światło'], [SwitchEvent])

    r = Recognizer(dom, currentLocation=k)
    r.recognise("WŁĄCZ światlo w kuchni")


if __name__ == '__main__':
    main()
