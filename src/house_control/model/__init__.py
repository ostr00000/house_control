import logging
import pickle
import time

from decorator import decorator

from house_control.model._model import Model as _Model

logger = logging.getLogger(__name__)


@decorator
def timeDec(fun, *args, **kwargs):
    t0 = time.time()
    res = fun(*args, **kwargs)
    logger.debug(f'Total time {fun.__name__}: {time.time() - t0}')
    return res


class _ModelWrapper:
    def __init__(self, fileName: str):
        self.fileName = fileName
        self._model = None

    @property
    def model(self):
        if self._model is None:
            try:
                self._load()
            except IOError:
                self._create()
                self._save()
        return self._model

    @timeDec
    def _load(self):
        with open(self.fileName, 'rb') as file:
            self._model = pickle.load(file)
        logger.info(f'Model {self.fileName} loaded')

    @timeDec
    def _create(self):
        self._model = _Model()
        logger.info('Model created')

    @timeDec
    def _save(self):
        with open(self.fileName, 'wb') as file:
            pickle.dump(self._model, file)
        logger.info('Model saved')


_model = _ModelWrapper('model.pickle')


def getModel():
    return _model.model
