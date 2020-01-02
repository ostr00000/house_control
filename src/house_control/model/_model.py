from __future__ import annotations
import logging
from collections import defaultdict
from typing import Dict, List, Set, TYPE_CHECKING, Iterable

from house_control.config import DICTIONARY_FILE

if TYPE_CHECKING:
    from house_control.model.location import Loc
    from house_control.model.device import Device
    from house_control.event import BaseHouseEvent

logger = logging.getLogger(__name__)


class Model:

    def __init__(self):
        self.wordsDict: Dict[str, str] = {}
        self.reverseWordsDict: Dict[str, List[str]] = defaultdict(list)
        self.initWordDicts()
        self.reverseWordsDict = dict(self.reverseWordsDict)

    def initWordDicts(self):
        with open(DICTIONARY_FILE) as dicFile:
            for lineNum, line in enumerate(dicFile):  # type: (int, str)
                words = [w.strip() for w in line.split(',')]
                try:
                    baseWord = words[0]
                except KeyError:
                    logger.warning(f"Not found valid words in line {lineNum}")
                    continue

                for word in words:
                    # too many words
                    # if word in self.wordsDict:
                    #     logger.warning(f"Word '{word}' already exist in dictionary - "
                    #                    f"overriding its base word to '{baseWord}'")

                    self.wordsDict[word] = baseWord

                self.reverseWordsDict[baseWord] = words

    def initModelAliases(self, *rootLocations):
        for rootLocation in rootLocations:
            for location in rootLocation:
                self.updateLocation(location)
                self.updateDevices(*location.devices)

    def updateLocation(self, location: Loc):
        names = set(location.aliases)
        names.add(location.name)
        for newAliases in self.aliasesGenerator(names):
            location.aliases.update(newAliases)

    def updateDevices(self, *devices: Device):
        for dev in devices:
            for newAliases in self.aliasesGenerator(dev.aliases):
                dev.aliases.update(newAliases)

    def updateEvent(self, event: BaseHouseEvent):
        for key, names in event.aliases.iterOverGroup():
            newAliases = self.aliasesGenerator(names)
            for newAlias in newAliases:
                event.aliases.addAliases(key, newAlias)

    def aliasesGenerator(self, names: Set[str]) -> Iterable[List[str]]:
        for longName in set(names):
            for name in longName.lower().split():
                try:
                    otherAliases = self.reverseWordsDict[name]
                except KeyError:
                    try:
                        otherAliases = self.reverseWordsDict[self.wordsDict[name]]
                    except KeyError:
                        logger.error(f"Invalid configuration - cannot find word '{name}'")
                        continue

                yield otherAliases
