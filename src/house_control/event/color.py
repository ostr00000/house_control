from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet
from house_control.exceptions import UnknownAction


class ColorEvent(BaseHouseEvent):
    colorMap = {
        'ciepły': 'warm',
        'zimny': 'cold',
        'żółty': 'yellow',
        'pomarańczowy': 'orange',
        'czerwony': 'red',
        'niebieski': 'blue',
        'fioletowy': 'purple',
        'zielony': 'green',
    }
    aliases = AliasSet(*tuple(colorMap.keys()), 'ustaw')

    def __str__(self):
        for i, colorCode in enumerate(self.colorMap.values()):
            if self.isInGroup(i):
                if i in (0, 1):
                    return f"{colorCode} {self.device}"
                return f"set {self.device} color {colorCode}"

        raise UnknownAction(f"Cannot recognize color: {self.command.sequence}")
