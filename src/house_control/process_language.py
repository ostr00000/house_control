from house_control.model.command import Command


def baseProcessing(command: str) -> Command:
    return Command(command.lower().split())


def getBaseVerb(command: str):
    """Move verb to base form"""
    return command.split(' ')[0] + 'yć'  # TODO


def getNouns(command):
    return [
        command.split(' ')[1],
        command.split(' ')[3] + 'a',
    ]
