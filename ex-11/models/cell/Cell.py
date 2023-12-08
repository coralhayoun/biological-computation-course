class Cell:
    def __init__(self, row, column, cell_parameters):
        self.row = row
        self.column = column
        self.current_parameters = cell_parameters
        self.next_parameters = cell_parameters
