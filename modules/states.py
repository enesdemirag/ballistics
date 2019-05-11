from enum import Enum

class BallState(Enum):
    PENDING = -1
    FIRE = 0
    HIT = 1
    MISS = 2
