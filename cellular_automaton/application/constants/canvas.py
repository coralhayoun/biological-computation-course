from application.models.cell.cell_wind import WindDirection
from application.models.cell.cell_element import CellElement
from application.models.cell.cell_weather_condition import CellWeatherCondition

compass_symbols = {
    WindDirection.NORTH.value : "\u2191",     # unicode arrow up
    WindDirection.EAST.value : "\u2192",     # unicode arrow right
    WindDirection.WEST.value : "\u2190",     # unicode arrow left
    WindDirection.SOUTH.value : "\u2193",     # unicode arrow down
}

elements_color = {
    CellElement.LAND.value: "#D2B48C",
    CellElement.SEA.value: "#3399FF",
    CellElement.ICEBURG.value: "#CCFFFF",
    CellElement.FOREST.value: "#90EE90",
    CellElement.CITY.value: "#828282",
    CellElement.FIRED.value: "#E34234",
}

weather_conditions_color = {
    CellWeatherCondition.CLOUDY.value : "#FFFFFF",
    CellWeatherCondition.RAINY.value : "#808080",
}