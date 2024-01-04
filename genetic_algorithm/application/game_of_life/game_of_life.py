#this is an efficient game of life implementation taken from https://www.madelyneriksen.com/python-game-of-life
#in this file, GameOfLife class inherits from the built-in 'dict' class and keeps only the grid alive cells.

class GameOfLife(dict):
    def __init__(self, grid_size, *args, **kwargs):
        self.grid_size = grid_size
        super(GameOfLife, self).__init__(*args, **kwargs)

    def __missing__(self, *args, **kwargs):
        return 0

    def get_size(self):
        return len(self)

    def get_cell_neighbors(self, x, y):
        x_coordinates = (x-1, x, x+1)
        y_coordinates = (y-1, y, y+1)
        neighbors = []

        for x in x_coordinates:
            for y in y_coordinates:
                neighbors.append((x, y))
        
        return neighbors

    def get_alive_neighbors(self, x, y):
        alived_neighbors = 0
        for neighbor_x, neighbor_y in self.get_cell_neighbors(x,y):
            alived_neighbors += self[neighbor_x, neighbor_y]
        
        return alived_neighbors

    def determine_cell_aliveness(self, x, y):
        alived_neighbors = self.get_alive_neighbors(x,y)
        cell = self[x, y]
        alive, dead = [], []

        #alive by reproduction
        if alived_neighbors == 3 and not cell:
            alive.append((x, y))
        #dies by overpopulation or underpopulation
        elif alived_neighbors < 3 or alived_neighbors > 4 and cell:
            dead.append((x, y))

        return alive, dead

    def play_game_iteration(self):
        alive_cells, dead_cells, generation_cells = [], [], []

        for x, y in self.keys():
            generation_cells.extend(self.get_cell_neighbors(x,y))

        for x, y in generation_cells:
            step_live, step_dead = self.determine_cell_aliveness(x, y)
            alive_cells += step_live
            dead_cells += step_dead
        
        #keep alive cells only
        for x, y in dead_cells:
            if self[x, y]:
                del self[x, y]
        for x, y in alive_cells:
            if (0 <= x < self.grid_size and 0 <= y < self.grid_size):
                self[x, y] = 1
        
        return (alive_cells, dead_cells)