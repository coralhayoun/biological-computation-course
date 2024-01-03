from cellular_automaton.models.automaton.cellular_automaton import CellularAutomaton
from cellular_automaton.models.automaton.neighborhood.neighborhood import Neighborhood, NeighborhoodName
from transition_rules import transition_rules

class GameOfLifeCell:
    def __init__(self, alive):
        self.alive = alive

class GameOfLife:
    def __init__(self, cells_matrix):
        self.automaton = CellularAutomaton(cells_matrix, Neighborhood(NeighborhoodName.MOORE), transition_rules)
    
    def run_iteration(self):
        self.automaton.update_cells_generation()
