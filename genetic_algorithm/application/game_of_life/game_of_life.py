import copy

from core.cellular_automaton import CellularAutomaton
from core.neighborhood.neighborhood import Neighborhood, NeighborhoodName
from application.game_of_life.transition_rules import transition_rules

class GameOfLifeCell:
    def __init__(self, alive):
        self.alive = alive

class GameOfLife:
    def __init__(self, cells_matrix):
        self.automaton = CellularAutomaton(cells_matrix, Neighborhood(NeighborhoodName.MOORE), transition_rules, 20)
        self.cells_matrix = cells_matrix
        self.history = []

        self.max_alive_cells = 0
        self.max_alive_cells_generation = 0
    
    def run_iteration(self):
        self.automaton.update_cells_generation()
    
    def play_whole_game(self):
        while self.automaton.current_generation <= self.automaton.generation_limit:
            self.automaton.update_cells_generation()
            self.cells_matrix = self.automaton.cells_matrix
            self.history.append(copy.deepcopy(self.automaton.cells_matrix))

            current_alive_cells = sum(cell.alive for row in self.automaton.cells_matrix for cell in row)
            if current_alive_cells > self.max_alive_cells:
                self.max_alive_cells = current_alive_cells
                self.max_alive_cells_generation = self.automaton.current_generation
    
    def is_idle(self):
        return self.automaton.cells_matrix in self.history

