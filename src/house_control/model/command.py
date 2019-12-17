from dataclasses import dataclass
from typing import List, Set


@dataclass
class Command:
    sequence: List[str]
    set: Set[str] = None

    def __post_init__(self):
        self.set = set(self.sequence)
