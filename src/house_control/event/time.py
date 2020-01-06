from house_control.event import BaseHouseEvent
from house_control.event.base import AliasSet
from house_control.exceptions import UnknownAction
from house_control.model.numbers import scanNumberGen


class TimeEvent(BaseHouseEvent):
    aliases = AliasSet('ustaw')

    def __str__(self):
        return f"set {self.device} time {self.getTime()}"

    def getTime(self):
        time = [str(num) for num in scanNumberGen(self.command.sequence)][:2]

        if not time:
            raise UnknownAction(f"Invalid time format {self.command}")

        if len(time) == 1:
            time.append('00')

        hours = time[0]
        minutes = time[1].rjust(2, '0')
        return f"{hours}:{minutes}"
