import os

from application.factories.cell_factory import CellFactory
from application.models.cell.cell_element import CellElement

cell_factory = CellFactory()

world_elements = []
for element in CellElement:
    world_elements.append(str(element.value))

class CellsMatrixFactory:
    def create_cells_matrix(self, rows, columns, cells_file):
        return self.init_cells_matrix(rows, columns, cells_file)

    def init_cells_matrix(self, rows, columns, cells_file):
        elements_matrix = self.create_elements_matrix(rows, columns, cells_file)
        cells_matrix = self.generate_matrix(rows, columns)

        for row in range(rows):
            for column in range(columns):
                cell_element = elements_matrix[row][column]
                cells_matrix[row][column] = cell_factory.create_cell(cell_element, row, column)

        return cells_matrix


    def create_elements_matrix(self, rows, columns, cells_file):
        elements_matrix = self.generate_matrix(rows, columns)
        file_path = self.get_file_path(cells_file)

        with open(file_path, 'r') as file:
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
        for item in CellElement:
            if str(item.value) == value:
                return item
            
    def get_file_path(self, cells_file):
        script_directory = os.path.dirname(os.path.realpath(__file__))
        relative_path_to_file = os.path.join('..', 'files', cells_file)

        return os.path.normpath(os.path.join(script_directory, relative_path_to_file))
