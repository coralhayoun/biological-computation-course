import copy

from utils.utils import generate_matrix

class CellularAutomaton:
    def __init__(self, cells_matrix, neighborhood, transition_rules):
        self.rows = len(cells_matrix)
        self.columns = len(cells_matrix[0])
        self.cells_matrix = cells_matrix
        self.neighborhood = neighborhood
        self.transition_rules = transition_rules

        self.current_generation = 0

    def update_cells_generation(self):
        new_cells_matrix = generate_matrix(self.rows, self.columns)

        for row in range(self.rows):
            for column in range(self.columns):
                neighbors = self.neighborhood.neighborhood_getter((row, column), self.cells_matrix)
                new_cell = self.run_transition_rules(self.cells_matrix[row][column], neighbors)
                new_cells_matrix[row][column] = new_cell
        
        #swap between the current cells matrix to the new one
        self.cells_matrix[:], new_cells_matrix[:] = new_cells_matrix[:], self.cells_matrix[:]

        self.current_generation += 1

    def run_transition_rules(self, cell, neighbors):
        new_cell = copy.deepcopy(cell)
        
        for rule in self.transition_rules:
          new_cell = rule(new_cell, neighbors)  

        return new_cell
    

    