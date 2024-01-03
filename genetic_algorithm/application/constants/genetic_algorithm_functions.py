
from application.game_of_life.game_of_life import GameOfLife
from core.crossover import single_point_crossover
from core.mutation import mutation

def cells_crossover(parent1, parent2):
    return GameOfLife(single_point_crossover(parent1.cells_matrix, parent2.cells_matrix))

def cell_mutation(cell):
    return GameOfLife(mutation(cell.cells_matrix, 0.2))

def cell_fitness(cell):
    cell.play_whole_game()
    print("done playing for the round")
    return cell.max_alive_cells

    