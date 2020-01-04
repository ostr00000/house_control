from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet
from house_control.model.command import Command
from house_control.model.device import Device


class SwitchEvent(BaseHouseEvent):
    aliases = AliasSet(('włącz', 'załącz', 'załączać'), 'wyłącz')

    def __init__(self, device: Device, command: Command):
        super().__init__(device, command)

    def __str__(self):
        return f"{'on' if self.isInGroup(0) else 'off'} {self.device}"
