import statistics

from factories.cells_matrix_factory import CellsMatrixFactory
from models.automaton.cellular_automaton import CellularAutomaton
from models.automaton.neighborhood.neighborhood import NeighborhoodName, Neighborhood
from constants.transition_rules import transition_rules

from models.ui.canvas import Canvas

def create_daily_temperaturev_file(daily_temp_list, yearly_avg_temp, yearly_std_dev_temp):
    temperatures = open("daily_temperature.txt", "w")
    normalaized_temperatures = open("daily_temperature_normalized.txt", "w")

    for daily_temperature in daily_temp_list:
        temperatures.write("{}\n".format(daily_temperature))
        daily_temperature_normalaized = (daily_temperature - yearly_avg_temp) / yearly_std_dev_temp
        normalaized_temperatures.write("{}\n".format(daily_temperature_normalaized))

    temperatures.close()
    normalaized_temperatures.close()

def create_daily_air_pollution_file(daily_pol_list, yearly_avg_pol, yearly_std_dev_pol):
    air_pollutions = open("daily_air_pollution.txt", "w")
    normalaized_air_pollutions = open("daily_air_pollution_normalized.txt", "w")
    
    for daily_air_pollution in daily_pol_list:
        air_pollutions.write("{}\n".format(daily_air_pollution))
        air_pollutions_normalaized = (daily_air_pollution - yearly_avg_pol) / yearly_std_dev_pol
        normalaized_air_pollutions.write("{}\n".format(air_pollutions_normalaized))
    
    air_pollutions.close()
    normalaized_air_pollutions.close()

cells_matrix_factory = CellsMatrixFactory()
rows = 15
columns = 15
cells_file = 'big-world-elements.dat'

cells_matrix = cells_matrix_factory.create_cells_matrix(rows, columns, cells_file)

automation = CellularAutomaton(cells_matrix, Neighborhood(NeighborhoodName.NEUMANN), transition_rules)
canvas = Canvas(automation)
canvas.init_canvas()

#yearly_temperature_average = statistics.mean(canvas.daily_temperature_avg)
#yearly_temperature_standart_deviation = statistics.pstdev(canvas.daily_temperature_avg)
#create_daily_air_pollution_file(canvas.daily_temperature_avg, yearly_temperature_average, yearly_temperature_standart_deviation)

#yearly_air_pol_average = statistics.mean(canvas.daily_air_pollution_avg)
#yearly_ail_pol_standart_deviation = statistics.pstdev(canvas.daily_air_pollution_avg)
#create_daily_air_pollution_file(canvas.daily_air_pollution_avg, yearly_air_pol_average, yearly_ail_pol_standart_deviation)

