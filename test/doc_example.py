import xlrd


def xlsTestGenerator():
    XLS_FILE = 'dane-testowe.xls'
    workbook = xlrd.open_workbook(XLS_FILE)
    sheet = workbook.sheet_by_index(0)

    for command, symbol, alternative in sheet.get_rows():
        yield command.value, symbol.value


def testFromXls():
    for command, symbol in xlsTestGenerator():
        print("OK")
