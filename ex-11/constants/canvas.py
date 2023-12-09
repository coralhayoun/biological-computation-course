from models.automaton.cell.cell_wind import WindDirection
from models.automaton.cell.cell_element import CellElement
from models.automaton.cell.cell_weather_condition import CellWeatherCondition

compass_symbols = {
    WindDirection.NORTH.value : "\u2191",     # unicode arrow up
    WindDirection.EAST.value : "\u2192",     # unicode arrow right
    WindDirection.WEST.value : "\u2190",     # unicode arrow left
    WindDirection.SOUTH.value : "\u2193",     # unicode arrow down
}

elements_color = {
    CellElement.LAND.value: "#994C00",
    CellElement.SEA.value: "#3399FF",
    CellElement.ICEBURG.value: "#CCFFFF",
    CellElement.FOREST.value: "#009900",
    CellElement.CITY.value: "#A0A0A0",
    CellElement.FIRED.value: "#FF8000",
}

weather_conditions_color = {
    CellWeatherCondition.CLOUDY.value : "#FFFFFF",
    CellWeatherCondition.RAINY.value : "#808080",
    CellWeatherCondition.REGULAR.value : "#FFFFFF",
}