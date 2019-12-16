from house_control.device import Device


class EventNotFound:
    pass


class LocationNotFound:
    pass


class DeviceNotFound:
    def __init__(self, *maybeDevice: Device):
        self.maybeDevice = maybeDevice

    def __repr__(self):
        return 'Maybe: ' + ','.join(d.name for d in self.maybeDevice)
