from __future__ import annotations

import logging
from typing import Type, TYPE_CHECKING, Iterable, Union

from house_control.model import getModel, convertToTuple
from house_control.model.command import Command
from house_control.model.device.code_name import generateCodeName

if TYPE_CHECKING:
    from house_control.event import BaseHouseEvent
    from house_control.model.location import Loc

logger = logging.getLogger(__name__)


class Device:
    """
    Representation of device in specific location.
    Device can use aliases.
    Device start default action.
    It is possible to create special aggregation device containing other devices -
    but all devices must have same interface.
    """
    def __init__(self, name: str,
                 loc: Loc,
                 *aliases: Iterable[str],
                 actions: Iterable[Type[BaseHouseEvent]] = (),
                 defaultAction: Type[BaseHouseEvent] = None,
                 aggr: Iterable[Device] = None,
                 codeName: str = None,
                 requiredNames: Union[str, Iterable[str]] = None,
                 ):
        """
        :param requiredNames: define words that must (or must not) be present in command
            All required names must be present.
            To define word that cannot be present use '!' ex.:
                ('ala', '!kot')
        """

        self.name = name
        self.loc = loc
        self.defaultAction = defaultAction
        self.codeName = generateCodeName() if codeName is None else codeName

        self.aggr = convertToTuple(aggr)
        assert (self.aggr is None or any(all(isinstance(obj, k) for obj in self.aggr)
                                         for k in type(self.aggr[0]).__mro__))

        self.requiredNames = convertToTuple(requiredNames)
        assert (self.requiredNames is None
                or len(self.requiredNames) > 0 and all(len(rn) > 0 for rn in requiredNames))

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

    def isRequirementMeet(self, cmd: Command) -> bool:
        if self.requiredNames:
            model = getModel()

            for requiredName in self.requiredNames:
                negative = requiredName[0] == '!'
                if negative:
                    requiredName = requiredName[1:]

                try:
                    requiredNameAliases = model.reverseWordsDict[requiredName]
                except KeyError:
                    logger.error(f"Cannot find '{requiredName}' in model")
                    continue

                if negative:
                    ok = all(k not in requiredNameAliases for k in cmd.sequence)
                else:
                    ok = any(k in requiredNameAliases for k in cmd.sequence)

                if not ok:
                    return False
        return True

    def __repr__(self):
        return f'{self.name} in [{self.loc}]'

    def __str__(self):
        return self.codeName

    def __hash__(self):
        return hash((self.name, frozenset(self.aliases)))
