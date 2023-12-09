import tkinter as tk

from constants.canvas import compass_symbols, elements_color, weather_conditions_color

class Canvas:
    def __init__(self, cells_matrix):
        self.cells_matrix = cells_matrix
        self.rows = len(cells_matrix)
        self.columns = len(cells_matrix[0])
        self.current_generation = 0
        self.generation_number = 365

        self.refresh_rate = 30
        self.cell_size = 50
        self.canvas_cells = [([0]*self.rows) for i in range(self.columns)]

    def init_canvas(self):
        root = tk.Tk()
        root.title("Maman 11 - Cellular Automaton World Simulation")
        lable = tk.Label(root, text="Generation {}".format(self.current_generation), font="bold")
        lable.pack()

        window_height = self.rows * self.cell_size
        window_width = self.columns * self.cell_size

        self.canvas = tk.Canvas(root, height=window_height, width=window_width, bg="white")
        self.canvas.pack()
        
        self.init_canvas_grid()
        self.color_canvas_grid()

        root.mainloop()


    def init_canvas_grid(self):
        cg = 0.13  # cloud_margin_gap, unit: cell size percentage
        
        for row in range(self.rows):
            for column in range(self.columns):
                canvas_square_id = self.canvas.create_rectangle(
                    column * self.cell_size, 
                    row * self.cell_size, 
                    (column + 1) * self.cell_size, 
                    (row + 1)*self.cell_size
                )
                canvas_text_id = self.canvas.create_text(
                    (column + 0.5) * self.cell_size, 
                    (row + 0.25) * self.cell_size, 
                    font=("Ariel 8 bold")
                )
                canvas_cloud_id = self.canvas.create_oval(
                    (column + cg) * self.cell_size, 
                    (row + 0.5 + cg) * self.cell_size, 
                    (column + 1 - cg) * self.cell_size, 
                    (row + 1 - cg) * self.cell_size, 
                    width=0
                )

                self.canvas_cells[row][column] = (canvas_square_id, canvas_text_id, canvas_cloud_id)

    def color_canvas_grid(self):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells_matrix[row][column]

                canvas_cell_text = compass_symbols[cell.wind.direction.value]
                canvas_cell_color = elements_color[cell.element.value]
                canvas_cell_cloud = weather_conditions_color[cell.weather_condition.value]
                
                (canvas_square_id, canvas_text_id, canvas_cloud_id) = self.canvas_cells[row][column]

                self.canvas.itemconfig(canvas_square_id, fill=canvas_cell_color)
                self.canvas.itemconfig(canvas_text_id, text=canvas_cell_text)

                if (canvas_cell_cloud != None):
                    self.canvas.itemconfig(canvas_cloud_id, fill=canvas_cell_cloud)
                else:
                    self.canvas.itemconfig(canvas_cloud_id, fill="")   # ~~ stopped