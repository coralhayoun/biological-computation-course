import copy

from core.cellular_automaton import CellularAutomaton
from core.neighborhood.neighborhood import Neighborhood, NeighborhoodName
from application.game_of_life.transition_rules import transition_rules

class GameOfLifeCell:
    def __init__(self, alive):
        self.alive = alive

class GameOfLife:
    def __init__(self, cells_matrix):
        self.automaton = CellularAutomaton(cells_matrix, Neighborhood(NeighborhoodName.MOORE), transition_rules, 200)
        self.cells_matrix = cells_matrix
        self.history = []

        self.max_alive_cells = sum(cell.alive for row in self.cells_matrix for cell in row)
        self.max_alive_cells_generation = 0
    
    def run_iteration(self):
        self.automaton.update_cells_generation()
    
    def play_whole_game(self):
        while self.automaton.current_generation <= self.automaton.generation_limit and self.is_idle() == False:
            self.history.append(copy.deepcopy(self.automaton.cells_matrix))
            self.automaton.update_cells_generation()
            self.cells_matrix = self.automaton.cells_matrix

            current_alive_cells = sum(cell.alive for row in self.automaton.cells_matrix for cell in row)
            if current_alive_cells > self.max_alive_cells:
                self.max_alive_cells = current_alive_cells
                self.max_alive_cells_generation = self.automaton.current_generation
        print(self.automaton.current_generation)
    
    def is_idle(self):
        for cells_matrix in self.history:
            if all(obj1.alive == obj2.alive for row1, row2 in zip(cells_matrix, self.cells_matrix) for obj1, obj2 in zip(row1, row2)):
                return True

        return False

