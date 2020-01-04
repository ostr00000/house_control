class RecogniseException(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = dict(kwargs)

    def __str__(self):
        res = ''
        if args := ','.join(str(a) for a in self.args):
            res += args
        if kwargs := ','.join(f'{k}={v}' for k, v in self.kwargs.items()):
            if res:
                res += ', '
            res += kwargs
        return res


class UnknownAction(RecogniseException):
    def __str__(self):
        return f"Cannot recognize action {super().__str__()}"


class UnknownLocation(RecogniseException):
    def __str__(self):
        return f"Cannot recognize location {super().__str__()}"


class UnknownDevice(RecogniseException):
    def __str__(self):
        return f"Cannot recognize device {super().__str__()}"
