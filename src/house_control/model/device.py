from dataclasses import field, dataclass
from typing import Type, List, Set

import house_control.model.location as location
from house_control.event import BaseHouseEvent


@dataclass
class Device:
    name: str
    loc: 'location.Loc'
    aliases: Set[str] = field(default_factory=set)
    actions: List[Type[BaseHouseEvent]] = field(default_factory=list)

    def __post_init__(self):
        loc = self.loc
        while loc:
            loc.devices.append(self)
            loc = loc.parent
