from abc import ABC


class BaseHouseEvent(ABC):
    name = ''
    aliases = set()
