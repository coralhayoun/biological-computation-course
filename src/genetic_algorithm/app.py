import random
import os
import sys

# for cellular_automaton folder importing
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, "cellular_automaton"))
sys.path.insert(0, parent_dir)

from models.game_of_life.game_of_life import GameOfLifeCell, GameOfLife
from models.game_of_life.game_of_life_ui import GameOfLifeUi
from utils.utils import generate_matrix

rows = 30
columns = 30
cells_matrix = generate_matrix(rows, columns)

for row in range(rows):
    for column in range(columns):
        cells_matrix[row][column] = GameOfLifeCell(random.random() < 0.5)

game_of_life = GameOfLife(cells_matrix)
ui = GameOfLifeUi(game_of_life)
ui.init_canvas()
      



