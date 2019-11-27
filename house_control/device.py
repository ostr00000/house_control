from dataclasses import field, dataclass
from typing import Type, List

import house_control.location as location
from house_control.event import MyEvent


@dataclass
class Device:
    name: str
    loc: location.Loc
    aliases: List[str] = field(default_factory=list)
    actions: List[Type[MyEvent]] = field(default_factory=list)

    def __post_init__(self):
        loc = self.loc
        while loc:
            loc.devices.append(self)
            loc = loc.parent
