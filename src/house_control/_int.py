
class Switchable:
    def turnOn(self):
        raise NotImplementedError

    def turnOff(self):
        raise NotImplementedError

    def switch(self, active):
        return self.turnOn() if active else self.turnOff()


class Lamp(Switchable):
    def turnOn(self):
        print("Light")

    def turnOff(self):
        print("Dark")

