class Command:
    def __init__(self, commandText: str):
        self.sequence = commandText.lower().split()
        self.set = set(filter(lambda x: len(x) > 2 and '%' not in x, self.sequence))
        if '%' in commandText:
            self.set.add('%')

    def __str__(self):
        return ' '.join(self.sequence)
