letter = 'A'
number = 0


def incCodeNameLetter():
    global letter
    letter = chr(ord(letter) + 1)
    global number
    number = 0


def generateCodeName():
    global number
    number += 1
    return f'{letter}{number}'
