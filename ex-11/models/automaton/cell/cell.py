class Cell:
    def __init__(self, element, temperature, wind, is_cloudy, air_pollution = 0.08):
        self.element = element
        self.wind = wind
        self.is_cloudy = is_cloudy
        self.air_pollution = air_pollution
        self.temperature = temperature
    
    def to_string(self):
        print("element: {}, temperature: {}, is_cloudy: {}".format(self.element.value, self.temperature, self.is_cloudy))
