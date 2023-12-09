from factories.cells_matrix_factory import CellsMatrixFactory
from models.automaton.cellular_automaton import CellularAutomaton
from models.automaton.neighborhood.neighborhood import NeighborhoodName, Neighborhood
from constants.transition_rules import transition_rules
cells_matrix_factory = CellsMatrixFactory()

rows = 15
columns = 15

cells_matrix = cells_matrix_factory.create_cells_matrix(rows, columns)

automation = CellularAutomaton(cells_matrix, Neighborhood(NeighborhoodName.NEUMANN), transition_rules)
automation.update_cells_generation()

