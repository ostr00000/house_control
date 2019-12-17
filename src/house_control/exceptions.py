class RecogniseException(Exception):
    pass


class UnknownAction(RecogniseException):
    def __str__(self):
        return "Cannot recognize action"


class UnknownLocation(RecogniseException):
    def __str__(self):
        return "Cannot recognize location"


class UnknownDevice(RecogniseException):
    def __str__(self):
        return "Cannot recognize device"
