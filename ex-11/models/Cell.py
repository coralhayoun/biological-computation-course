from models.Element import Element

temperature_mapping ={
    Element.LAND.name: 25,
    Element.SEA.name: 20,
    Element.ICEBURG.name: -15,
    Element.FOREST.name: 20,
    Element.CITY.name: 27,
}

class Cell:
    def __init__(self, element, wind, clouds, air_pollution):
        self.element = element
        self.wind = wind
        self.clouds = clouds
        self.air_pollution = air_pollution
        self.temperature = self.get_temperature(element)

    
    def get_temperature(self, element):
        return temperature_mapping[element.name]
    
    def to_string(self):
        print(self.temperature)
