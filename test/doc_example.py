from typing import Iterator, Tuple

import xlrd

from house_control.house_configuration import house
from house_control.recognizer import Recognizer


def xlsTestGenerator() -> Iterator[Tuple[str, str]]:
    XLS_FILE = 'dane-testowe.xls'
    workbook = xlrd.open_workbook(XLS_FILE)
    sheet = workbook.sheet_by_index(0)

    for command, symbol, alternative in sheet.get_rows():
        yield command.value, symbol.value


def testFromXls():
    """Non empty results 91/215"""
    rec = Recognizer(house)

    total = 0
    nonEmpty = 0
    for command, symbol in xlsTestGenerator():
        total += 1
        event = rec.recognizeOptionalEvent(command)
        if event is not None:
            nonEmpty += 1
        print(f"Recognized: {repr(event).ljust(20)}, Expected: {symbol}")

    print(f"Non empty results {nonEmpty}/{total}")
    print("OK")
