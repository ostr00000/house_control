from __future__ import annotations

from abc import ABC, abstractmethod
from itertools import islice
from typing import TYPE_CHECKING, Iterable, Tuple, Union, Set, ItemsView

from house_control.exceptions import RecogniseException

if TYPE_CHECKING:
    from house_control.model.device import Device
    from house_control.model.command import Command


class AliasSet(set):
    """
    Object can have multiple subsets.
    This mechanism allow to check if a word belongs to any of categories,
    and later to check each categories separably.
    Each of words can update its alias individually.
    """

    def __init__(self, *mainWords: Union[str, Tuple[str, ...]]):
        """
        Each argument create new group
        ex. 3 groups and the second group has 2 words:
            AliasSet('ala', ('ma', 'posiada'), 'kota')
        """
        super().__init__()
        self._data = {}
        for mainWord in mainWords:
            if isinstance(mainWord, tuple):
                self.update(mainWord)
                key: str = mainWord[0]
                val: Set[str] = set(mainWord)

            else:
                self.add(mainWord)
                key = mainWord
                val = {mainWord}

            self._data[key] = val

    def getGroup(self, n: int):
        assert n <= len(self._data), f'Invalid group {n} - max group {len(self._data)}'
        return next(islice(self._data.values(), n, None))

    def iterOverGroup(self) -> ItemsView[str, Set[str]]:
        return self._data.items()

    def addAliases(self, mainWord: str, newValues: Iterable[str]) -> None:
        self._data[mainWord].update(newValues)
        self.update(newValues)


class BaseHouseEvent(ABC):
    """
    Base class for all events.
    Due to search by __subclasses__ in initialization from model,
    all event must inherit from this class.
    """

    name = ''
    aliases: AliasSet

    def __init__(self, device: Device, command: Command):
        """Raise exception if color is invalid"""
        self.device = device
        self.command = command
        self.__str__()  # test exception

    @classmethod
    def checkIfValid(cls, command: Command):
        """
        Check if command can be recognized as event.
        If return False event is excluded from possible solution.
        It is useful when command must contain certain words.
        """
        try:
            # noinspection PyTypeChecker
            str(cls('check', command))
        except RecogniseException:
            return False
        return True

    def __repr__(self):
        """This function return readable information about device"""
        return f"{type(self).__name__} for device '{repr(self.device)}'"

    @abstractmethod
    def __str__(self):
        """This function return symbolic code of action with device. It is used in tests."""
        raise NotImplementedError

    def isInGroup(self, groupNumber: int):
        """Check if command belongs to groupNumber"""
        return any(elem in self.command.set for elem in self.aliases.getGroup(groupNumber))
