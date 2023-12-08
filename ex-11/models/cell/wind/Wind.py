from models.cell.wind.WindDirection import WindDirection

class Wind:
    def __init__(self, speed = 0.5, direction = WindDirection.NORTH):
        self.speed = speed
        self.direction = direction