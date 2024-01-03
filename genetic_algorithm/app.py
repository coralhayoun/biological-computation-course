import random
import os
import sys

# for cellular_automaton folder importing
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, "cellular_automaton"))
sys.path.insert(0, parent_dir)

from application.game_of_life.game_of_life import GameOfLifeCell, GameOfLife
from application.game_of_life.game_of_life_ui import GameOfLifeUi
from utils.utils import generate_matrix

rows = 30
columns = 30

def generate_cells_matrix():
    cells_matrix = generate_matrix(rows, columns)

    for row in range(rows):
        for column in range(columns):
            cells_matrix[row][column] = GameOfLifeCell(random.random() < 0.5)
    
    return cells_matrix

#game_of_life = GameOfLife(generate_cells_matrix())
#ui = GameOfLifeUi(game_of_life)
#ui.init_canvas()

def generate_population():
    for i in range(10):
        genome = GameOfLife(generate_cells_matrix())




