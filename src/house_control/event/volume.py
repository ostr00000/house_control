from house_control.event import BaseHouseEvent


class VolumeEvent(BaseHouseEvent):
    aliases = {'głośniej', 'ciszej', 'podgłośnić', 'ściszyć'}

    def __repr__(self):
        return 'set <DEV> vol <N>'
        return 'vol_up <N>'
        return 'vol_down <N>'
