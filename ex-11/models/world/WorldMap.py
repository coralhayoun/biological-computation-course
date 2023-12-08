from factories.WorldMatrixFactory import WorldMatrixFactory

world_matrix_factory = WorldMatrixFactory()

class WorldMap:
    def __init__(self, rows, columns, cell_size, map_file):
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.world_matrix = world_matrix_factory.create_world_matrix(rows, columns, map_file)