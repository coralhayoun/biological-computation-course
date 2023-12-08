from models.cell.CellParameters import CellParameters
from models.cell.Cell import Cell
from models.cell.wind.WindDirection import WindDirection
from models.cell.wind.Wind import Wind

class CellFactory:
    def create_cell(self, element, row, column):
        is_cloudy = self.init_is_cloudy(row, column)
        wind_direction = self.init_wind_direction(row, column)
        wind = Wind(wind_direction = wind_direction)
        cell_parameters = CellParameters(element, wind, is_cloudy)

        return Cell(cell_parameters)

    def init_wind_direction(self, row, column):
        if (row + column) %2 == 0:
            return WindDirection.NORTH
        else:
            return WindDirection.WEST

    #create cloud for each 6-th cell
    def init_is_cloudy(self, row, column):
        return (row + column) % 6 == 0
