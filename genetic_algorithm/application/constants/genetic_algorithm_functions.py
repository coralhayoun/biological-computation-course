
from application.game_of_life.game_of_life import GameOfLife
from core.crossover import nth_points_crossover
from core.mutation import mutation

def cells_crossover(parent1, parent2):
    return GameOfLife(nth_points_crossover(parent1.cells_matrix, parent2.cells_matrix, 3))

def cell_mutation(cell):
    return GameOfLife(mutation(cell.cells_matrix, 0.2))

def cell_fitness(cell):
    cell.play_whole_game()
    return cell.max_alive_cells

    