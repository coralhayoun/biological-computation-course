from models.automaton.cell.cell import Cell
from models.automaton.cell.cell_wind import WindDirection
from models.automaton.cell.cell_wind import CellWind
from models.automaton.cell.cell_element import CellElement
from models.automaton.cell.cell_weather_condition import CellWeatherCondition

element_to_temperature_mapping ={
    CellElement.LAND.name: 25,
    CellElement.SEA.name: 15,
    CellElement.ICEBURG.name: -30,
    CellElement.FOREST.name: 20,
    CellElement.CITY.name: 27,
    CellElement.FIRED.name: 50,
}

class CellFactory:
    def create_cell(self, element, row, column):
        weather_condition = self.init_weather_condition(row, column)
        wind_direction = self.init_wind_direction(row, column)
        wind = CellWind(direction = wind_direction)
        temperatue = element_to_temperature_mapping[element.name]

        return Cell(element, temperatue, wind, weather_condition)

    def init_wind_direction(self, row, column):
        if (row + column) %4 == 0:
            return WindDirection.NORTH
        elif (row + column) %4 == 1:
            return WindDirection.SOUTH
        elif (row + column) %4 == 2:
            return WindDirection.EAST
        else:
            return WindDirection.WEST

    def init_weather_condition(self, row, column):
        if (row + column) % 12 == 0:
            return CellWeatherCondition.RAINY
        elif (row + column) % 6 == 0:
            return CellWeatherCondition.CLOUDY
        
        return CellWeatherCondition.REGULAR
        
