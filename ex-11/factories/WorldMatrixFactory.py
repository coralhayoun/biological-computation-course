from factories.CellFactory import CellFactory
from models.Element import Element

world_elements = list(Element.__members__.values())
cell_factory = CellFactory()

class WorldMatrixFactory:
    def create_world_matrix(self, rows, columns, map_file):
        return self.init_cells_matrix(rows, columns, map_file)

    def init_cells_matrix(self, rows, columns, map_file):
        elements_matrix = self.create_elements_matrix(rows, columns, map_file)
        cells_matrix = self.generate_matrix(rows, columns)

        for row in range(rows):
            for column in range(columns):
                cell_element = elements_matrix[row][column]
                cells_matrix[row][column] = cell_factory.create_cell(cell_element, row, column)

        return cells_matrix


    def create_elements_matrix(self, rows, columns, map_file):
        elements_matrix = self.generate_matrix(rows, columns)
        
        with open(map_file, 'r') as file:
            for row in range(rows):
                for column in range(columns):
                    element_value = file.read(1)

                    while element_value not in world_elements:
                        element_value = file.read(1)
                    
                    elements_matrix[row][column] = self.get_element_by_value(element_value)

        return elements_matrix

    def generate_matrix(self, rows, columns):
            return [([0]*rows) for i in range(columns)]

    def get_element_by_value(self, value):
        for item in Element:
            if item.value == value:
                return item