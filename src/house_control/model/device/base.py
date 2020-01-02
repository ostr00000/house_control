from __future__ import annotations

from typing import Type, TYPE_CHECKING, Iterable

from house_control.model import getModel
from house_control.model.device.code_name import generateCodeName

if TYPE_CHECKING:
    from house_control.event import BaseHouseEvent
    from house_control.model.location import Loc


class Device:
    def __init__(self, name: str,
                 loc: Loc,
                 actions: Iterable[Type[BaseHouseEvent]] = (),
                 defaultAction: Type[BaseHouseEvent] = None,
                 aggr: Iterable[Device] = None,
                 codeName: str = None,
                 *aliases: Iterable[str]):
        self.name = name
        self.loc = loc
        self.defaultAction = defaultAction
        self.aggr = list(aggr) if aggr else None
        assert (self.aggr is None or any(all(isinstance(obj, k) for obj in self.aggr)
                                         for k in type(self.aggr[0]).__mro__))

        self.codeName = generateCodeName() if codeName is None else codeName
        self.aliases = set(aliases)
        self.initAliases()

        self.actions = list(actions)
        self.initActions()

        loc.devices.append(self)
        getModel().updateDevices(self)

    def initActions(self):
        pass

    def initAliases(self):
        pass

    def __repr__(self):
        return f'{self.name} in [{self.loc}]'

    def __str__(self):
        return self.codeName

    def __hash__(self):
        return hash((self.name, frozenset(self.aliases)))
