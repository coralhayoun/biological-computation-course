import random
import os
import sys

# for cellular_automaton folder importing
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, "cellular_automaton"))
sys.path.insert(0, parent_dir)

from core.genetic_algorithm import GeneticAlgorithm
from application.constants.genetic_algorithm_functions import cells_crossover, cell_fitness, cell_mutation
from application.game_of_life.game_of_life import GameOfLifeCell, GameOfLife
from application.game_of_life.game_of_life_board import GameOfLifeBoard
from utils.utils import generate_matrix

rows = 30
columns = 30

def generate_cells_matrix():
    cells_matrix = generate_matrix(rows, columns)

    for row in range(rows):
        for column in range(columns):
            cells_matrix[row][column] = GameOfLifeCell(random.random() < 0.5)
    
    return cells_matrix


def generate_population():
    population = []
    for i in range(10):
        population.append(GameOfLife(generate_cells_matrix()))
    
    return population

genetic_algorithm = GeneticAlgorithm(generate_population(), cell_fitness, cells_crossover, cell_mutation, 20)
best = genetic_algorithm.run_algorithm()
GameOfLifeBoard(best)

