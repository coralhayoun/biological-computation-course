import tkinter as tk

class Canvas:
    def __init__(self, automaton):
        self.automaton = automaton

        self.cells_matrix = automaton.cells_matrix
        self.callback = automaton.update_cells_generation
        self.rows = len(automaton.cells_matrix)
        self.columns = len(automaton.cells_matrix[0])

        self.refresh_rate = 15
        self.cell_size = 50
        self.alive_color = 'orange'
        self.dead_color = 'white'
        self.canvas_cells = [([0]*self.rows) for i in range(self.columns)]
    
    def init_canvas(self):
        self.root = tk.Tk()
        self.root.title("Conway's Game of Life")
        self.lable = tk.Label(self.root, text="Generation {}".format(self.automaton.current_generation), font="bold")
        self.lable.pack()

        window_height = self.rows * self.cell_size
        window_width = self.columns * self.cell_size

        self.canvas = tk.Canvas(self.root, height=window_height, width=window_width, bg="white")
        self.canvas.pack()
        self.root.resizable(False, False)
        
        self.init_canvas_grid()

        self.root.after(self.refresh_rate, self.update_canvas)
        self.root.mainloop()
    
    def init_canvas_grid(self):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells_matrix[row][column]

                x1 = row * self.cell_size
                y1 = column * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                cell_color = self.alive_color if cell.alive else self.dead_color

                canvas_square_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=cell_color, outline="black")
                self.canvas_cells[row][column] = canvas_square_id
    
    def update_canvas(self):
        if self.automaton.current_generation < self.automaton.generation_limit:
            print("updating canvas")
            self.automaton.update_cells_generation()
            
            self.update_canvas_colors()
            print(self.automaton.current_generation)
            self.lable.config(text="Generation {}".format(self.automaton.current_generation))
            self.root.after(self.refresh_rate, self.update_canvas)
        else:
            self.lable.config(text="Generation {}, simulation finished!".format(self.automaton.current_generation))
        
    def update_canvas_colors(self):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells_matrix[row][column]
                cell_color = self.alive_color if cell.alive else self.dead_color

                canvas_square_id = self.canvas_cells[row][column]
                self.canvas.itemconfig(canvas_square_id, fill=cell_color)
                self.canvas_cells[row][column] = canvas_square_id

    