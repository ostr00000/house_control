from house_control.event import BaseHouseEvent
from house_control.event.base import BaseHouseEvent

from house_control.model import Model

from .switch import SwitchEvent


def initEvents():
    model = Model()
    model.updateAliases(*BaseHouseEvent.__subclasses__())


initEvents()
