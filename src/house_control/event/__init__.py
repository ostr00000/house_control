import pkgutil
from house_control.event.base import BaseHouseEvent


def _importAllModules():
    for loader, module_name, is_pkg in pkgutil.walk_packages(
            __path__, prefix='house_control.event.'):
        __import__(module_name)


def _initEvents():
    from house_control.model import getModel
    getModel().updateAliases(*BaseHouseEvent.__subclasses__())


_importAllModules()
_initEvents()
