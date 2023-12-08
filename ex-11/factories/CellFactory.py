from models.cell.CellParameters import CellParameters
from models.cell.Cell import Cell
from models.cell.wind.WindDirection import WindDirection
from models.cell.wind.Wind import Wind
from models.world.Element import Element

element_to_temperature_mapping ={
    Element.LAND.name: 25,
    Element.SEA.name: 20,
    Element.ICEBURG.name: -15,
    Element.FOREST.name: 20,
    Element.CITY.name: 27,
}

class CellFactory:
    def create_cell(self, element, row, column):
        is_cloudy = self.init_is_cloudy(row, column)
        wind_direction = self.init_wind_direction(row, column)
        wind = Wind(wind_direction = wind_direction)
        temperatue = element_to_temperature_mapping[element.value]
        cell_parameters = CellParameters(element, temperatue, wind, is_cloudy)

        return Cell(row, column, cell_parameters)

    def init_wind_direction(self, row, column):
        if (row + column) %2 == 0:
            return WindDirection.NORTH
        else:
            return WindDirection.WEST

    #create clouds for each 6-th cell
    def init_is_cloudy(self, row, column):
        return (row + column) % 6 == 0
