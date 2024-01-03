import tkinter as tk
import statistics

from application.constants.canvas import compass_symbols, elements_color, weather_conditions_color

class Canvas:
    def __init__(self, automaton):
        self.automaton = automaton

        self.cells_matrix = automaton.cells_matrix
        self.callback = automaton.update_cells_generation
        self.rows = len(automaton.cells_matrix)
        self.columns = len(automaton.cells_matrix[0])

        self.refresh_rate = 15
        self.cell_size = 50
        self.canvas_cells = [([0]*self.rows) for i in range(self.columns)]

        self.daily_temperature_avg = []
        self.daily_air_pollution_avg = []

    def update_canvas(self):
        if self.automaton.current_generation < self.automaton.generation_limit:
            print("updating canvas")
            self.automaton.update_cells_generation()
            
            self.color_canvas_grid()
            print(self.automaton.current_generation)
            self.lable.config(text="Generation {}".format(self.automaton.current_generation))
            self.sub_lable.config(text=self.get_canvas_subtitle())
            self.root.after(self.refresh_rate, self.update_canvas)
        else:
            self.lable.config(text="Generation {}, simulation finished!".format(self.automaton.current_generation))

    def init_canvas(self):
        self.root = tk.Tk()
        self.root.title("maman 11 - Cellular Automaton Simulation")
        self.lable = tk.Label(self.root, text="Generation {}".format(self.automaton.current_generation), font="bold")
        self.sub_lable = tk.Label(self.root, text=self.get_canvas_subtitle())
        self.lable.pack()
        self.sub_lable.pack()


        window_height = self.rows * self.cell_size
        window_width = self.columns * self.cell_size

        self.canvas = tk.Canvas(self.root, height=window_height, width=window_width, bg="white")
        self.canvas.pack()
        
        self.init_canvas_grid()
        self.color_canvas_grid()

        self.root.after(self.refresh_rate, self.update_canvas)
        self.root.mainloop()

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

                canvas_cell_text = self.get_cell_text(cell)
                canvas_cell_color = elements_color[cell.element.value]
                canvas_cell_cloud = None
                
                if cell.weather_condition.value in weather_conditions_color:
                    canvas_cell_cloud = weather_conditions_color[cell.weather_condition.value]
                
                (canvas_square_id, canvas_text_id, canvas_cloud_id) = self.canvas_cells[row][column]

                self.canvas.itemconfig(canvas_square_id, fill=canvas_cell_color)
                self.canvas.itemconfig(canvas_text_id, text=canvas_cell_text)

                if (canvas_cell_cloud != None):
                    self.canvas.itemconfig(canvas_cloud_id, fill=canvas_cell_cloud)
                else:
                    self.canvas.itemconfig(canvas_cloud_id, fill="")

    def get_cell_text(self, cell):
        cell_wind_direction = compass_symbols[cell.wind.direction.value]
        cell_temperature = int(cell.temperature)  # adding unicode celcius degeress symbol
        cell_air_pollution = round(cell.air_pollution * 100, 1)

        return "{} {}\u2103\n P:{}%".format(cell_wind_direction, cell_temperature, cell_air_pollution)

    def get_canvas_subtitle(self):
        temperature_list = self.get_temperature_list()
        air_pollution_list = self.get_air_pollution_list()

        temperature_avg = round(statistics.mean(temperature_list), 1)
        air_pollution_avg = round(statistics.mean(air_pollution_list) * 100, 2)
        temperature_std_dev = round(statistics.pstdev(temperature_list), 1)
        air_pollution_std_dev = round( statistics.pstdev(air_pollution_list)*100, 2)

        self.daily_temperature_avg.append(temperature_avg)
        self.daily_air_pollution_avg.append(air_pollution_avg)

        line1 = "Average temperature: {}\u2103   \t Average air Pollution: {}%\n".format(temperature_avg, air_pollution_avg)
        line2 = "Standart deviation: {}\u2103 \t\t Standart deviation: {}%".format(temperature_std_dev,  air_pollution_std_dev)

        return line1 + line2
    
    def get_temperature_list(self): 
        temperatures = []

        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells_matrix[row][column]
                temperatures.append(cell.temperature)
        
        return temperatures
    
    def get_air_pollution_list(self): 
        air_pollutions = []

        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells_matrix[row][column]
                air_pollutions.append(cell.air_pollution)
        
        return air_pollutions