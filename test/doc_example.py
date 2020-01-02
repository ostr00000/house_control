import logging
from random import seed
from typing import Iterator, Tuple

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


def testFromXls():
    """Non empty results 115/214"""
    rec = Recognizer(house)

    total = 0
    nonEmpty = 0
    gen = xlsTestGenerator()
    header = next(gen)
    logger.info(f'{" " * 12}{header[0].ljust(30)} : {header[1]}')

    for command, symbol in gen:
        total += 1
        event = rec.recognizeOptionalEvent(command)
        if event is not None:
            nonEmpty += 1

        logger.info(
            f"Recognized: {str(event).ljust(30)} : "
            f"Expected: {symbol.ljust(15)} : "
            f"{repr(event).ljust(30)} : "
        )
        rec.recognizeOptionalEvent(command)

    logger.info(f"Non empty results {nonEmpty}/{total}")
