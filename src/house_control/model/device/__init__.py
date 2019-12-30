from house_control.event.brightness import BrightnessEvent
from house_control.event.channel import ChannelEvent
from house_control.event.color import ColorEvent
from house_control.event.speed import SpeedEvent
from house_control.event.switch import SwitchEvent
from house_control.event.time import TimeEvent
from house_control.event.toggle import ToggleEvent
from house_control.event.vertical import VerticalEvent
from house_control.event.volume import VolumeEvent
from house_control.model.device.base import Device


class SwitchDevice(Device):
    def initActions(self):
        self.initActions()
        self.actions.append(SwitchEvent)
        self.actions.append(ToggleEvent)


class Computer(SwitchDevice):
    pass


class Monitor(SwitchDevice):
    pass


class Light(SwitchDevice):
    pass


class ColorLight(Light):
    def initActions(self):
        super().initActions()
        self.actions.append(ColorEvent)


class BrightnessLight(Light):
    def initActions(self):
        super().initActions()
        self.actions.append(BrightnessEvent)


class Fan(SwitchDevice):
    pass


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


class TV(Radio):
    pass


class AlarClock(Device):
    def initActions(self):
        super().initActions()
        self.actions.append(SwitchEvent)
        self.actions.append(TimeEvent)


class Shutter(Device):
    def initActions(self):
        super().initActions()
        self.actions.append(VerticalEvent)
