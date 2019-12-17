from house_control.event.base import BaseHouseEvent
from house_control.event.switch import SwitchEvent


def _initEvents():
    from house_control.model import getModel
    getModel().updateAliases(*BaseHouseEvent.__subclasses__())


_initEvents()
