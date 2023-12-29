class Cell:
    def __init__(self, element, temperature, wind, weather_condition, air_pollution = 0.01):
        self.element = element
        self.wind = wind
        self.weather_condition = weather_condition
        self.air_pollution = air_pollution
        self.temperature = temperature
