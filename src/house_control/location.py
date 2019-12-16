from dataclasses import dataclass, field
from typing import List

import house_control.device as device


@dataclass
class Loc:
    name: str
    aliases: List[str] = field(default_factory=list)
    parent: 'Loc' = None
    children: List['Loc'] = field(default_factory=list)
    devices: List[device.Device] = field(default_factory=list)

    def __post_init__(self):
        if self.parent:
            self.parent.children.append(self)

    def __iter__(self):
        for child in self.children:
            yield child
            yield from child
