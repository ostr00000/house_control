from __future__ import annotations

from abc import ABC, abstractmethod
from itertools import islice
from typing import TYPE_CHECKING, Iterable, Tuple, Union, Iterator, Set, ItemsView

if TYPE_CHECKING:
    from house_control.model.device import Device
    from house_control.model.command import Command


class AliasSet(set):
    """Each argument create new group"""

    def __init__(self, *mainWords: Union[str, Tuple[str, ...]]):
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
        return next(islice(self._data.values(), n, None))

    def iterOverGroup(self) -> ItemsView[str, Set[str]]:
        return self._data.items()

    def addAliases(self, mainWord: str, newValues: Iterable[str]) -> None:
        self._data[mainWord].update(newValues)
        self.update(newValues)


class BaseHouseEvent(ABC):
    name = ''
    aliases: AliasSet

    def __init__(self, device: Device, command: Command):
        self.device = device
        self.command = command

    def __str__(self):
        return f"{type(self).__name__} for device '{self.device}'"

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError
