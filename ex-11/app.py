from factories.cells_matrix_factory import CellsMatrixFactory
from models.automaton.cellular_automaton import CellularAutomaton
from models.automaton.neighborhood.neighborhood import NeighborhoodName, Neighborhood
from constants.transition_rules import transition_rules

from models.ui.canvas import Canvas

cells_matrix_factory = CellsMatrixFactory()

rows = 15
columns = 15
cells_file = 'little-world-elements.dat'

cells_matrix = cells_matrix_factory.create_cells_matrix(rows, columns, cells_file)

automation = CellularAutomaton(cells_matrix, Neighborhood(NeighborhoodName.NEUMANN), transition_rules)
canvas = Canvas(cells_matrix)
canvas.init_canvas()
automation.update_cells_generation()

