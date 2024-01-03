import random

from cellular_automaton import print

from cellular_automaton.models.automaton.cellular_automaton import CellularAutomaton

from models.game_of_life.game_of_life import GameOfLifeCell, GameOfLife
from models.game_of_life.game_of_life_ui import GameOfLifeUi
from cellular_automaton.utils.utils import generate_matrix

rows = 30
columns = 30
cells_matrix = generate_matrix(rows, columns)

for row in range(rows):
    for column in range(columns):
        cells_matrix[row][column] = GameOfLifeCell(random.random() < 0.5)

game_of_life = GameOfLife(cells_matrix)
ui = GameOfLifeUi()
ui.init_canvas()
      



