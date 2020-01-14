from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Set, TYPE_CHECKING

from house_control.model import getModel

if TYPE_CHECKING:
    from house_control.model.device import Device


@dataclass
class Loc:
    """
    Object represent logical position.
    Can contains other locations and devices.
    Location has name, but it is possible to assign many aliases.
    """
    name: str
    aliases: Set[str] = field(default_factory=set)
    parent: Loc = None
    children: List[Loc] = field(default_factory=list)
    devices: List[Device] = field(default_factory=list)

    def __post_init__(self):
        if self.parent:
            self.parent.children.append(self)

        getModel().updateLocation(self)

    def __str__(self):
        return f'{self.name} in [{self.parent}]' if self.parent else self.name

    def __iter__(self):
        yield self
        for child in self.children:
            yield from child

    def __hash__(self):
        return hash((self.name, frozenset(self.aliases)))

    def __contains__(self, item):
        assert isinstance(item, Loc)
        while item:
            if item == self:
                return True
            item = item.parent
        return False

    def deep(self):
        cur = self
        counter = 1
        while cur.parent:
            counter += 1
            cur = cur.parent
        return counter
