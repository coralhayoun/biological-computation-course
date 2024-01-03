from enum import Enum

class WindDirection(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class CellWind:
    def __init__(self, speed = 0.5, direction = WindDirection.NORTH):
        self.speed = speed
        self.direction = direction