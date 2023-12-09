from factories.cells_matrix_factory import CellsMatrixFactory
from models.automaton.cellular_automaton import CellularAutomaton
from models.automaton.neighborhood.neighborhood import NeighborhoodName, Neighborhood
from constants.transition_rules import transition_rules

from models.ui.canvas import Canvas
from models.ui.graph_displater import GraphDisplayer

# init celular automaton
cells_matrix_factory = CellsMatrixFactory()
rows = 15
columns = 15
cells_file = 'big-world-elements.dat'

cells_matrix = cells_matrix_factory.create_cells_matrix(rows, columns, cells_file)
automation = CellularAutomaton(cells_matrix, Neighborhood(NeighborhoodName.NEUMANN), transition_rules)

# init canvas (ui representation)
canvas = Canvas(automation)
canvas.init_canvas()

# display graph over the data
graph_displayer = GraphDisplayer(canvas.daily_temperature_avg, canvas.daily_air_pollution_avg)
graph_displayer.display_linear_graph()