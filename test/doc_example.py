import logging
from functools import partial, partialmethod
from random import seed
from typing import Iterator, Tuple, Callable

import xlrd

from house_control.event import BaseHouseEvent
from house_control.house_configuration import house
from house_control.recognizer import Recognizer

logger = logging.getLogger(__name__)
seed(123)


def xlsTestGenerator() -> Iterator[Tuple[str, str, str]]:
    XLS_FILE = 'dane-testowe.xls'
    workbook = xlrd.open_workbook(XLS_FILE)
    sheet = workbook.sheet_by_index(0)

    for command, symbol, alternative in sheet.get_rows():
        yield command.value, symbol.value, alternative.value


class Color:
    _NORMAL = '\033[0m'
    _RED = '\033[31m'
    _GREEN = '\033[32m'
    _MAGENTA = '\033[35m'

    @staticmethod
    def _logInColor(text, color=None, level=logging.INFO):
        logger.log(level, f'{color} {text} {Color._NORMAL}')

    red = partialmethod(_logInColor, color=_RED)
    magenta = partialmethod(_logInColor, color=_MAGENTA)
    green = partialmethod(_logInColor, color=_GREEN)


class ResultCmp:
    def __init__(self):
        self.total = 0
        self.nonEmpty = 0
        self.fullyRecognizedCommand = 0

    def addResult(self, event: BaseHouseEvent, *expected: str, command):
        if event is None:
            result = 'error'
            color = Color.red
        else:
            result = str(event)
            self.nonEmpty += 1
            color = Color.magenta

        self.total += 1
        if result in expected:
            self.fullyRecognizedCommand += 1
            color: Callable = Color.green

        color(
            f"Recognized: {str(event).ljust(22)} "
            f"Expected: {expected[0].ljust(18)} "
            f"Command: {command.ljust(40)} "
            f"{repr(event).ljust(30)} "
        )

    def logSummary(self):
        logger.info(f"Non empty results {self.nonEmpty}/{self.total}")
        logger.info(f"Fully recognized command {self.fullyRecognizedCommand}/{self.total}")


def testFromXls():
    """
    Non empty results: 195/214
    Fully recognized command: 70/214
    """
    rec = Recognizer(house)
    cmp = ResultCmp()
    gen = xlsTestGenerator()

    headers = next(gen)
    logger.info(':'.join(header.ljust(30) for header in headers))

    for command, symbol, alternativeSymbol in gen:
        event = rec.recognizeOptionalEvent(command)
        cmp.addResult(event, symbol, alternativeSymbol, command=command)

    cmp.logSummary()
