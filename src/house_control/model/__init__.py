from house_control.model._model import Model as _Model

_model = None


def getModel():
    global _model

    if not _model:
        _model = _Model()
    return _model
