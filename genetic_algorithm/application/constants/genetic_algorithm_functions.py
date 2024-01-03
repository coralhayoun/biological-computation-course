
from core.crossover import nth_points_crossover
from core.mutation import mutation

def cells_crossover(parent1, parent2):
    nth_points_crossover(parent1.cells_matrix, parent2.cells_matrix, 3)

def cell_mutation(cell):
    mutation(cell.cells_matrix, 0.2)

    