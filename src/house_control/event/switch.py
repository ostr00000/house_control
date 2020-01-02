from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet
from house_control.model.command import Command
from house_control.model.device import Device


class SwitchEvent(BaseHouseEvent):
    aliases = AliasSet(('włącz', 'załącz'), 'wyłącz')

    def __init__(self, device: Device, command: Command):
        super().__init__(device, command)

    def isOn(self):
        return any(elem in self.command.set for elem in self.aliases.getGroup(0))

    def __repr__(self):
        return 'on' if self.isOn() else 'off'
