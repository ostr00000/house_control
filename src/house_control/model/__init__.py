import logging
from collections import defaultdict
from typing import Dict, List, Iterator, Protocol, Set

from house_control.config import DICTIONARY_FILE
from house_control.model.location import Loc

logger = logging.getLogger(__name__)


class AliasObject(Protocol):
    name: str
    aliases: Set[str]


class Model:

    def __init__(self, *rootLocations: Loc):
        self.rootLocations = rootLocations

        self.wordsDict: Dict[str, str] = {}
        self.reverseWordsDict: Dict[str, List[str]] = defaultdict(list)

        self.initWordDicts()
        self.initModelAliases()

    def initWordDicts(self):
        with open(DICTIONARY_FILE) as dicFile:
            for lineNum, line in enumerate(dicFile):

                words = list(filter(None, line.split()))
                try:
                    baseWord = words[0]
                except KeyError:
                    logger.warning(f"Not found valid words in line {lineNum}")
                    continue

                for word in words:
                    if word in self.wordsDict:
                        logger.warning(f"Word '{word}' already exist in dictionary - "
                                       f"overriding its base word to '{baseWord}'")

                    self.wordsDict[word] = baseWord

                self.reverseWordsDict[baseWord] = words

    def initModelAliases(self):
        for rootLocation in self.rootLocations:
            for location in rootLocation:
                self.updateAliases(location)
                self.updateAliases(*location.devices)

    def updateAliases(self, *aliasObjects: AliasObject):
        for aliasObject in aliasObjects:
            for otherAliases in self.aliasesGenerator(aliasObject):
                aliasObject.aliases.update(otherAliases)

    def aliasesGenerator(self, aliasObject: AliasObject) -> Iterator[List[str]]:
        names = set(aliasObject.aliases)
        names.add(aliasObject.name)

        for name in names:
            try:
                otherAliases = self.reverseWordsDict[name]
            except KeyError:
                try:
                    otherAliases = self.reverseWordsDict[self.wordsDict[name]]
                except KeyError:
                    logger.error(f"Invalid configuration - cannot find word '{name}'")
                    continue

            yield otherAliases
