from __future__ import annotations

from dataclasses import field, dataclass
from typing import Type, List, Set, TYPE_CHECKING, Optional

from house_control.model import getModel

if TYPE_CHECKING:
    from house_control.event import BaseHouseEvent
    from house_control.model.location import Loc


@dataclass
class Device:
    name: str
    loc: Loc
    aliases: Set[str] = field(default_factory=set)
    actions: List[Type[BaseHouseEvent]] = field(default_factory=list)
    defaultAction: Optional[Type[BaseHouseEvent]] = None

    def __post_init__(self):
        loc = self.loc
        while loc:
            loc.devices.append(self)
            loc = loc.parent

        getModel().updateAliases(self)
        self.initActions()

    def initActions(self):
        pass

    def __str__(self):
        return f'{self.name} in [{self.loc}]'

    def __hash__(self):
        return hash((self.name, frozenset(self.aliases)))
