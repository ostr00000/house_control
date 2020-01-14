import logging

from house_control.exceptions import RecogniseException


def main():
    from house_control.house_configuration import house
    from house_control.recognizer import Recognizer

    rec = Recognizer(house)
    try:
        event = rec.recognizeEvent('włącz światło w kuchni')
        print(event.__repr__())
    except RecogniseException as exc:
        print(exc)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
