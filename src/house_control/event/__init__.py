"""
This package load all modules from its directory,
then initialize events' aliases from model object.
"""
import pkgutil

from house_control.event.base import BaseHouseEvent


def _importAllModules():
    for loader, module_name, is_pkg in pkgutil.walk_packages(
            __path__, prefix='house_control.event.'):
        __import__(module_name)


def _initEvents():
    from house_control.model import getModel
    model = getModel()
    for event in BaseHouseEvent.__subclasses__():
        model.updateEvent(event)
    

_importAllModules()
_initEvents()
