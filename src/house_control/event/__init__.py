import pkgutil
from house_control.event.base import BaseHouseEvent


def _importModules():
    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module


def _initEvents():
    from house_control.model import getModel
    getModel().updateAliases(*BaseHouseEvent.__subclasses__())


_importModules()
_initEvents()
