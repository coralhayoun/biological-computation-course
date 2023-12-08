from factories.CellFactory import CellFactory
from models.Element import Element

world_elements = list(Element.__members__.values())
cell_factory = CellFactory()

class WorldFactory:
    def __init__(self, rows, columns, map_file):
        self.rows = rows
        self.columns = columns
        self.map_file = map_file
        self.cells_matrix = self.init_cells_matrix()

    def init_cells_matrix(self):
        elements_matrix = self.create_elements_matrix()
        cells_matrix = self.generate_matrix()

        for row in range(self.rows):
            for column in range(self.columns):
                cell_element = elements_matrix[row][column]
                cells_matrix[row][column] = cell_factory.create_cell(cell_element, row, column)

        return cells_matrix


    def create_elements_matrix(self):
        elements_matrix = self.generate_matrix()
        
        with open(self.map_file, 'r') as file:
            for row in range(self.rows):
                for column in range(self.columns):
                    element_value = file.read(1)

                    while element_value not in world_elements:
                        element_value = file.read(1)
                    
                    elements_matrix[row][column] = self.get_element_by_value(element_value)

        return elements_matrix

    def generate_matrix(self):
            return [([0]*self.rows) for i in range(self.columns)]

    def get_element_by_value(self, value):
        for item in Element:
            if item.value == value:
                return item