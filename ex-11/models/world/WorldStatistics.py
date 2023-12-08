import statistics

class WorldStatistics:
    def __init__(self, cells_matrix):
        temperatues = self.get_temperature_list(cells_matrix)
        air_pollutions = self.get_air_pollution_list(cells_matrix)

        self.temperature_average = statistics.mean(temperatues)
        self.air_pollution_average = statistics.mean(air_pollutions)
        self.temperature_std_dev = statistics.pstdev(temperatues)
        self.air_pollution_std_dev = statistics.pstdev(air_pollutions)

        self.pollution_heat_factor = 0.7  # how much 100% pollution will raise the temperture in a day (in celsius degrees)
        self.rain_cold_factor = 0.4       # how much will the temperature decrease when raining
        self.is_raining = False
    
    def get_temperature_list(self, cells_matrix):
        temperatues = []

        for row in cells_matrix:
            for column in row:
                cell = cells_matrix[row][column]
                temperatues.insert(cell.current_parameters.temperatue)

        return temperatues
    
    def get_air_pollution_list(self, cells_matrix):
        air_pollution = []

        for row in cells_matrix:
            for column in row:
                cell = cells_matrix[row][column]
                air_pollution.insert(cell.current_parameters.air_pollution)

        return air_pollution