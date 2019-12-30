import logging
from collections import defaultdict
from typing import Dict, List, Iterator, Protocol, Set, Union, Type

from house_control.config import DICTIONARY_FILE

logger = logging.getLogger(__name__)


class AliasObject(Protocol):
    name: str
    aliases: Set[str]


AliasAttribute = Union[AliasObject, Type[AliasObject]]


class Model:

    def __init__(self):
        self.wordsDict: Dict[str, str] = {}
        self.reverseWordsDict: Dict[str, List[str]] = defaultdict(list)
        self.initWordDicts()
        self.reverseWordsDict = dict(self.reverseWordsDict)
        logger.info('Model loaded')

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
                self.updateAliases(location)
                self.updateAliases(*location.devices)

    def updateAliases(self, *aliasObjects: AliasAttribute):
        for aliasObject in aliasObjects:
            for otherAliases in self.aliasesGenerator(aliasObject):
                aliasObject.aliases.update(otherAliases)

    def aliasesGenerator(self, aliasObject: AliasAttribute) -> Iterator[List[str]]:
        names = set(aliasObject.aliases)
        if getattr(aliasObject, 'name', False):
            names.add(aliasObject.name)

        for longName in names:
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
