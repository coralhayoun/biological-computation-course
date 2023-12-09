from models.automaton.neighborhood.neighborhood_name import NeighborhoodName

neighborhood_to_moves_mapping = {
    NeighborhoodName.NEUMANN: [(-1, 0), (0, 1), (1, 0), (0, -1)],
    NeighborhoodName.MOORE: [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ],
}

class Neighborhood:
    def __init__(self, neighborhood_name):
        self.neighborhood_name = neighborhood_name
        self.neighborhood_getter = self.init_neighborhood_getter(neighborhood_name)

    def init_neighborhood_getter(self, neighborhood_name):
        moves = neighborhood_to_moves_mapping[neighborhood_name.value]

        def neighbors_getter(cell_index, cells_matrix):
            return self.get_neighbors_by_moves(cell_index, cells_matrix, moves)
        
        return neighbors_getter


    def get_neighbors_by_moves(self, cell_index, cells_matrix, moves_array):
        neighbors = []

        rows = len(cells_matrix)
        columns = len(cells_matrix[0])
        (row, column) = cell_index

        for move in moves_array:
            new_row, new_col = row + move[0], column + move[1]
            new_row %= rows
            new_col %= columns

            neighbors.append(cells_matrix[new_row][new_col])

        return neighbors

