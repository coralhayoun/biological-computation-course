from models.automaton.cellular_automaton import CellularAutomaton
from models.automaton.neighborhood.neighborhood import Neighborhood, NeighborhoodName
from models.game_of_life.transition_rules import transition_rules

class GameOfLifeCell:
    def __init__(self, alive):
        self.alive = alive

class GameOfLife:
    def __init__(self, cells_matrix):
        self.automaton = CellularAutomaton(cells_matrix, Neighborhood(NeighborhoodName.MOORE), transition_rules, 20)
    
    def run_iteration(self):
        self.automaton.update_cells_generation()
