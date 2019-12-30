from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from house_control.model.device import Device
    from house_control.model.command import Command


class BaseHouseEvent(ABC):
    name = ''
    aliases = set()

    def __init__(self, device: Device, command: Command):
        self.device = device
        self.command = command

    def __str__(self):
        return f"{type(self).__name__} for device '{self.device}'"

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError
