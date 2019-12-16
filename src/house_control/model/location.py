from dataclasses import dataclass, field
from typing import List, Set

import house_control.model.device as device


@dataclass
class Loc:
    name: str
    aliases: Set[str] = field(default_factory=set)
    parent: 'Loc' = None
    children: List['Loc'] = field(default_factory=list)
    devices: List[device.Device] = field(default_factory=list)

    def __post_init__(self):
        if self.parent:
            self.parent.children.append(self)

    def __iter__(self):
        yield self
        for child in self.children:
            yield child
            yield from child
