class Cell:
    def __init__(self, element, temperature, wind, weather_condition, air_pollution = 0.08):
        self.element = element
        self.wind = wind
        self.weather_condition = weather_condition
        self.air_pollution = air_pollution
        self.temperature = temperature
    
    def to_string(self):
        print("element: {}, temperature: {}, weather: {}".format(self.element.value, self.temperature, self.weather_condition.name))
