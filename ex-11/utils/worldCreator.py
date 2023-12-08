from utils.CellFactory import CellFactory
from models.Element import Element

world_elements = list(Element.__members__.values())
cell_factory = CellFactory()

def create_cells_matrix(rows, columns, elements_matrix):
    cells_matrix = generate_matrix(rows, columns)

    for row in range(rows):
        for column in range(columns):
            cell_element = elements_matrix[row][column]
            cells_matrix[row][column] = cell_factory.create_cell(cell_element, row, column)

    return cells_matrix


def create_elements_matrix(rows, columns, map_file):
    elements_matrix = generate_matrix(rows, columns)
    
    with open(map_file, 'r') as file:
        for row in range(rows):
            for column in range(columns):
                element = file.read(1)

                while element not in world_elements:
                    element = file.read(1)
                
                elements_matrix[row][column] = get_element_by_value(element)

    return elements_matrix

def generate_matrix(rows, columns):
        return [([0]*rows) for i in range(columns)]

def get_element_by_value(value):
    for item in Element:
        if item.value == value:
            return item