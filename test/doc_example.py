import logging
from functools import partial, partialmethod
from random import seed
from typing import Iterator, Tuple, Callable

import xlrd

from house_control.house_configuration import house
from house_control.recognizer import Recognizer

logger = logging.getLogger(__name__)
seed(123)


def xlsTestGenerator() -> Iterator[Tuple[str, str]]:
    XLS_FILE = 'dane-testowe.xls'
    workbook = xlrd.open_workbook(XLS_FILE)
    sheet = workbook.sheet_by_index(0)

    for command, symbol, alternative in sheet.get_rows():
        yield command.value, symbol.value


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


def testFromXls():
    """
    Non empty results: 110/214
    Fully recognized command: 32/214
    """
    rec = Recognizer(house)

    total = 0
    nonEmpty = 0
    fullyRecognizedCommand = 0

    gen = xlsTestGenerator()
    header = next(gen)
    logger.info(f'{" " * 12}{header[0].ljust(30)} : {header[1]}')

    for command, symbol in gen:
        total += 1
        event = rec.recognizeOptionalEvent(command)
        if event is not None:
            nonEmpty += 1

        recognized = symbol == str(event)
        if recognized:
            fullyRecognizedCommand += 1

        if recognized:
            color: Callable = Color.green
        elif event is not None:
            color = Color.magenta
        else:
            color = Color.red

        color(
            f"Recognized: {str(event).ljust(22)} "
            f"Expected: {symbol.ljust(18)} "
            f"Command: {command.ljust(40)} "
            f"{repr(event).ljust(30)} "
        )

    logger.info(f"Non empty results {nonEmpty}/{total}")
    logger.info(f"Fully recognized command {fullyRecognizedCommand}/{total}")
