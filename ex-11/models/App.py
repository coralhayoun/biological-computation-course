import tkinter as tk

class App:
    def __init__(self, world):
        self.refresh_rate = 30
        self.gen_num = 365
        self.current_gen = 1
       
        self.world = world
        self.rows = self.world.world_map.rows
        self.cols = self.world.world_map.columns
        self.cell_size = self.world.world_map.cell_size

        self.canvas_cells = [([0]*self.rows) for i in range(self.columns)]

    def create_canvas(self):
        root = tk.Tk()
        root.title("Maman 11 - Cellular Automaton World Simulation")
        lable = tk.Label(root, text="Generation {}".format(self.current_gen), font="bold")
        lable.pack()

        window_height = self.rows * self.cell_size
        window_width = self.cols * self.cell_size
        #sub_lable = tk.Label(root, text=self._get_sub_label_text())
        #sub_lable.pack()

        canvas = tk.Canvas(root, height=window_height, width=window_width, bg="white")
        canvas.pack()
        
        #self.init_canvas_content()

    def init_canvas_content(self):
        print("creating canvas")
        cg = 0.13  # cloud_margin_gap, unit: cell size percentage
        for y in range(self.rows):
            for x in range(self.cols):
                canvas_square_id = self.canvas.create_rectangle(x*self.cell_size, y*self.cell_size, (x+1)*self.cell_size, (y+1)*self.cell_size)
                canvas_text_id = self.canvas.create_text((x+0.5)*self.cell_size, (y+0.25)*self.cell_size, font=("Ariel 8 bold"))
                canvas_cloud_id = self.canvas.create_oval((x+cg)*self.cell_size, (y+0.5+cg)*self.cell_size, (x+1-cg)*self.cell_size, (y+1-cg)*self.cell_size, width=0)
                self.canvas_cells[x][y] = (canvas_square_id, canvas_text_id, canvas_cloud_id)
        print("canvas created")

