from models.automaton.cell.cell_element import CellElement
from models.automaton.cell.cell_wind import WindDirection
from models.automaton.cell.cell_weather_condition import CellWeatherCondition
from constants.reverse_wind_directions import reverse_wind_directions

pollution_heat_factor = 0.5  # how much 100% pollution will raise the temperture in a day (in celsius degrees)
rain_cold_factor = 0.04       # how much will the temperature decrease when raining

def update_cell_wind(cell, neighbors):
    current_to_next_direction = {
        WindDirection.NORTH.name: WindDirection.WEST,
        WindDirection.WEST.name: WindDirection.NORTH,
        WindDirection.SOUTH.name: WindDirection.SOUTH,
        WindDirection.EAST.name: WindDirection.EAST
    }

    cell.wind.direction = current_to_next_direction[cell.wind.direction.name]

    return cell

def update_cell_air_pollution(cell, neighbors):
    # blowing some pollution away
    cell.air_pollution -= cell.air_pollution * cell.wind.speed * 0.05

    # neighbor blowing pollution towatd me
    for neighbor in neighbors:
        if neighbor.wind.direction == reverse_wind_directions[cell.wind.direction.name]:
            cell.air_pollution += neighbor.air_pollution * neighbor.wind.speed * 0.05
    
    # making sure air pollution is between 0% - 100%
    cell.air_pollution = min(1, cell.air_pollution)
    cell.air_pollution = max(0, cell.air_pollution)

    return cell

def update_cell_temperature(cell, neighbors):
    # raise temperature becuase of pollution
    cell.temperature += cell.air_pollution * pollution_heat_factor
    
    # decrease temperature because of cold
    if cell.weather_condition == CellWeatherCondition.RAINY and cell.temperature > 15:
        cell.temperature -= rain_cold_factor

    # temperature is affected by the neighbors
    avg_temperature = sum(neighbor.temperature for neighbor in neighbors) / len(neighbors) if neighbors else 0
    cell.temperature += (avg_temperature -cell.temperature) * 0.01

    return cell

def update_cell_element(cell, neighbors):
    if cell.element.name == CellElement.ICEBURG.name and cell.temperature > 0:
        cell.element = CellElement.SEA
    elif cell.element.name == CellElement.SEA.name and cell.temperature < 0:
        cell.element = CellElement.ICEBURG
    elif cell.element.name == CellElement.SEA.name and cell.temperature > 50:
        cell.element = CellElement.LAND
    elif cell.element.name == CellElement.FOREST.name and cell.temperature > 40:
        cell.element = CellElement.FIRED
    elif cell.element.name == CellElement.CITY.name and cell.temperature > 50:
        cell.element = CellElement.FIRED
    elif cell.element.name == CellElement.LAND.name and cell.temperature > 60:
        cell.element = CellElement.FIRED
    elif cell.element.name == CellElement.FIRED.name and cell.temperature < 30:
        cell.element = CellElement.CITY
    
    return cell

def update_cell_weather_condition(cell, neighbors):
    if cell.weather_condition != CellWeatherCondition.CLOUDY and cell.temperature > 10 and cell.temperature < 25:
        cell.weather_condition = CellWeatherCondition.CLOUDY

    elif cell.weather_condition != CellWeatherCondition.RAINY and cell.temperature < 10:
        cell.weather_condition = CellWeatherCondition.RAINY
    
    elif cell.weather_condition != CellWeatherCondition.REGULAR and cell.temperature > 25:
        cell.weather_condition = CellWeatherCondition.REGULAR

    return cell

transition_rules = [
    update_cell_wind,
    update_cell_air_pollution,
    update_cell_temperature,
    update_cell_element,
    update_cell_weather_condition,
]