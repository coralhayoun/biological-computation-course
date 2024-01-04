import copy
import tkinter as tk

class GameOfLifeUi:
    def __init__(self, game_of_life):
        self.game_of_life = copy.deepcopy(game_of_life)
        self.rows = game_of_life.grid_size
        self.columns = self.rows

        self.current_generation = 0
        self.canvas_cells = [([0]*self.rows) for i in range(self.columns)]

        self.cell_size = 10
        self.refresh_rate = 50
        self.alive_color = "blue"
        self.dead_color = "white"
        
        self.draw_canvas()
        self.draw_start_button()

        self.root.mainloop()

    def draw_canvas(self):
        self.root = tk.Tk()
        self.root.title("Conway's Game of Life")
        self.lable = tk.Label(self.root, text="Generation {}".format(self.current_generation), font="bold")
        self.lable.pack()

        window_height = self.rows * self.cell_size
        window_width = self.columns * self.cell_size

        self.canvas = tk.Canvas(self.root, height=window_height, width=window_width, bg="white")
        self.canvas.pack()
        self.root.resizable(False, False)

        self.draw_canvas_grid()

    def draw_canvas_grid(self):
        for x in range(self.rows):
            for y in range(self.columns):
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                cell_color = self.alive_color if (x,y) in self.game_of_life else self.dead_color
                canvas_square_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=cell_color, outline="black")
                self.canvas_cells[x][y] = canvas_square_id

    def update_canvas(self, alive, dead):
        self.lable.config(text="Generation {}".format(self.current_generation))

        if alive != None:
            for x,y in alive:
                if self.in_grid_bounderies(x,y):
                    canvas_square_id = self.canvas_cells[x][y]
                    self.canvas.itemconfig(canvas_square_id, fill=self.alive_color)
        
        if dead != None:
            for x,y in dead:
                if self.in_grid_bounderies(x,y):
                    canvas_square_id = self.canvas_cells[x][y]
                    self.canvas.itemconfig(canvas_square_id, fill=self.dead_color)

    def draw_start_button(self):
        self.start_button = tk.Button(self.root, text="Start", command=self.play_game_iteration)
        self.start_button.pack()

    def play_game_iteration(self):
        self.current_generation += 1

        alive, dead = self.game_of_life.play_game_iteration()
        self.update_canvas(alive, dead)

        self.root.after(self.refresh_rate, self.play_game_iteration)

    def in_grid_bounderies(self, x, y):
        return (0 <= x < self.rows and 0 <= y < self.columns)
