import logging
from typing import Iterator, List

from house_control.model import getModel

logger = logging.getLogger(__name__)


def findNumber(textList: List[str]):
    total = None
    for val in scanNumberGen(textList):
        if val is None:
            if total is None:
                continue
            else:
                break
        else:
            if total is None:
                total = val
            else:
                total += val

    return total


def scanSplitByChar(joinedNumbers: str, splitChar=':') -> Iterator[int]:
    ok = False
    for maybeNumber in joinedNumbers.split(splitChar):
        try:
            number = int(maybeNumber)
        except ValueError:
            continue
        ok = True
        yield number

    if not ok:
        logger.warning(f"Not found any number in {joinedNumbers}")


def scanNumberGen(textList: List[str]) -> Iterator[int]:
    model = getModel()
    for maybeNumber in textList:
        try:
            baseForm = model.wordsDict[maybeNumber]
        except KeyError:
            try:
                number = int(maybeNumber)
            except ValueError:
                if ':' in maybeNumber:
                    yield from scanSplitByChar(maybeNumber, ':')
                elif '%' in maybeNumber and maybeNumber != '%':
                    yield from scanSplitByChar(maybeNumber, '%')
                else:
                    logger.error(f'Unknown base form for {maybeNumber}')
            else:
                yield number
            continue

        try:
            number = ordinalNumbers[baseForm]
        except KeyError:
            try:
                number = cardinalNumbers[baseForm]
            except KeyError:
                continue

        yield number


cardinalNumbers = {
    'jeden': 1,
    'dwa': 2,
    'trzy': 3,
    'cztery': 4,
    'pięć': 5,
    'sześć': 6,
    'siedem': 7,
    'osiem': 8,
    'dziewięć': 9,
    'dziesięć': 10,
    'jedenaście': 11,
    'dwanaście': 12,
    'trzynaście': 13,
    'czternaście': 14,
    'piętnaście': 15,
    'szesnaście': 16,
    'siedemnaście': 17,
    'osiemnaście': 18,
    'dziewiętnaście': 19,
    'dwadzieścia': 20,
    'trzydzieści': 30,
    'czterdzieści': 40,
    'pięćdziesiąt': 50,
    'sześćdziesiąt': 60,
    'siedemdziesiąt': 70,
    'osiemdziesiąt': 80,
    'dziewięćdziesiąt': 90,
    'sto': 100,
}
ordinalNumbers = {
    'pierwszy': 1,
    'drugi': 2,
    'trzeci': 3,
    'czwarty': 4,
    'piąty': 5,
    'szósty': 6,
    'siódmy': 7,
    'ósmy': 8,
    'dziewiąty': 9,
    'dziesiąty': 10,
    'jedenasty': 11,
    'dwunasty': 12,
    'trzynasty': 13,
    'czternasty': 14,
    'piętnasty': 15,
    'szesnasty': 16,
    'siedemnasty': 17,
    'osiemnasty': 18,
    'dziewiętnasty': 19,
    'dwudziesty': 20,
    'trzydziesty': 30,
    'czterdziesty': 40,
    'pięćdziesiąty': 50,
    'sześćdziesiąty': 60,
    'siedemdziesiąty': 70,
    'osiemdziesiąty': 80,
    'dziewięćdziesiąty': 90,
    'setny': 100,
}
