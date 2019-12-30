class Command:
    def __init__(self, commandText: str):
        self.sequence = commandText.lower().split()
        self.set = set(filter(lambda x: len(x) > 2, self.sequence))

    def __str__(self):
        return ' '.join(self.sequence)
