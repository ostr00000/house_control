from house_control.event.brightness import BrightnessEvent
from house_control.event.channel import ChannelEvent
from house_control.event.color import ColorEvent
from house_control.event.speed import SpeedEvent
from house_control.event.switch import SwitchEvent
from house_control.event.time import TimeEvent
from house_control.event.toggle import ToggleEvent
from house_control.event.vertical import VerticalEvent
from house_control.event.volume import VolumeEvent
from house_control.model.device import Device


class SwitchDevice(Device):
    def initActions(self):
        self.actions.append(SwitchEvent)
        self.actions.append(ToggleEvent)
        self.defaultAction = ToggleEvent


class Computer(SwitchDevice):
    pass


class Monitor(SwitchDevice):
    def initAliases(self):
        super().initAliases()
        self.aliases.add('monitor')
        self.aliases.add('ekran')


class Light(SwitchDevice):
    def initAliases(self):
        super().initAliases()
        self.aliases.add('światło')
        self.aliases.add('oświetlenie')


class ColorLight(Light):
    def initActions(self):
        super().initActions()
        self.actions.append(ColorEvent)


class BrightnessLight(Light):
    def initActions(self):
        super().initActions()
        self.actions.append(BrightnessEvent)


class Fan(SwitchDevice):
    def initAliases(self):
        super().initAliases()
        self.aliases.add('wentylator')
        self.aliases.add('wiatrak')


class SpeedFan(Fan):
    def initActions(self):
        self.actions.append(SpeedEvent)


class Blower(SwitchDevice):
    pass


class Radio(SwitchDevice):
    def initActions(self):
        super().initActions()
        self.actions.append(ChannelEvent)
        self.actions.append(VolumeEvent)

    def initAliases(self):
        super().initAliases()
        self.aliases.add('radio')


class TV(Radio):
    def initAliases(self):
        super().initAliases()
        self.aliases.add('telewizor')
        self.aliases.add('TV')


class AlarClock(Device):
    def initActions(self):
        super().initActions()
        self.actions.append(SwitchEvent)
        self.actions.append(TimeEvent)
        self.defaultAction = SwitchEvent

    def initAliases(self):
        super().initAliases()
        self.aliases.add('budzik')


class Shutter(Device):
    def initActions(self):
        super().initActions()
        self.actions.append(VerticalEvent)
        self.defaultAction = VerticalEvent

    def initAliases(self):
        super().initAliases()
        self.aliases.add('rolety')
        self.aliases.add('żaluzje')
