from application.factories.cells_matrix_factory import CellsMatrixFactory
from core.cellular_automaton import CellularAutomaton
from core.neighborhood.neighborhood import NeighborhoodName, Neighborhood
from application.constants.transition_rules import transition_rules
from application.models.canvas import Canvas

# init celular automaton
cells_matrix_factory = CellsMatrixFactory()
rows = 15
columns = 15
cells_file = 'big-world-elements.dat'

cells_matrix = cells_matrix_factory.create_cells_matrix(rows, columns, cells_file)
automation = CellularAutomaton(cells_matrix, Neighborhood(NeighborhoodName.NEUMANN), transition_rules, 365)

# init canvas (ui representation)
canvas = Canvas(automation)
canvas.init_canvas()