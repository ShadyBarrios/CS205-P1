from enum import Enum

# just making these so that its easier to standardize stuff
class AlgosEnum(Enum):
    UNIFORM = 1
    MISPLACED = 2
    EUCLIDEAN = 3

class ActionsEnum(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class HeuristicsEnum(Enum):
    MISPLACED = 1
    EUCLIDEAN = 2