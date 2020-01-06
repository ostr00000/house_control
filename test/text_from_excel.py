import logging
from functools import partialmethod
from random import seed
from typing import Tuple, Callable, Union, Generator

import xlrd

from house_control.event import BaseHouseEvent
from house_control.house_configuration import house
from house_control.recognizer import Recognizer

logger = logging.getLogger(__name__)
seed(123)


def xlsTestGenerator() -> Generator[Union[Tuple[str, str, str], Tuple[str, str]], None, None]:
    XLS_FILE = 'dane-testowe.xls'
    workbook = xlrd.open_workbook(XLS_FILE)
    sheet = workbook.sheet_by_index(0)

    for commandCell, *symbolCells in sheet.get_rows():
        symbolCells = symbolCells[:3]
        ret = tuple(val for cell in symbolCells if (val := cell.value))
        yield (commandCell.value,) + ret


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
        result = 'error' if event is None else str(event)

        self.total += 1
        if result in expected:
            self.nonEmpty += 1
            self.fullyRecognizedCommand += 1
            color: Callable = Color.green
        elif event is not None:
            self.nonEmpty += 1
            color = Color.magenta
        else:
            color = Color.red

        color(
            f"Recognized: {str(event).ljust(22)} "
            f"Expected: {'|'.join(expected).ljust(18)} "
            f"Command: {command.ljust(40)} "
            f"{repr(event).ljust(30)} "
        )

        if result not in expected:  # DEBUG
            r = Recognizer(house)
            event = r.recognizeOptionalEvent(command)

    def logSummary(self):
        logger.info(f"Non empty results {self.nonEmpty}/{self.total}")
        logger.info(f"Fully recognized command {self.fullyRecognizedCommand}/{self.total}")


def testFromXls():
    """
    Non empty results: 189/214
    Fully recognized command: 114/214
    """
    rec = Recognizer(house)
    cmp = ResultCmp()
    gen = xlsTestGenerator()
    _headers = next(gen)

    for command, *symbols in gen:
        event = rec.recognizeOptionalEvent(command)
        cmp.addResult(event, *symbols, command=command)

    cmp.logSummary()
