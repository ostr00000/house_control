from __future__ import annotations

from typing import Type, List, TYPE_CHECKING, Iterable

from house_control.model import getModel

if TYPE_CHECKING:
    from house_control.event import BaseHouseEvent
    from house_control.model.location import Loc


class Device:
    def __init__(self, name: str, loc: Loc, aliases: Iterable[str] = (),
                 defaultAction: Type[BaseHouseEvent] = None):
        self.name = name
        self.loc = loc
        self.defaultAction = defaultAction

        self.aliases = set(aliases)
        self.initAliases()

        self.actions: List[Type[BaseHouseEvent]] = []
        self.initActions()

        self.addDeviceToParents()
        getModel().updateAliases(self)

    def addDeviceToParents(self):
        loc = self.loc
        while loc:
            loc.devices.append(self)
            loc = loc.parent

    def initActions(self):
        pass

    def initAliases(self):
        pass

    def __str__(self):
        return f'{self.name} in [{self.loc}]'

    def __hash__(self):
        return hash((self.name, frozenset(self.aliases)))
