from models.Element import Element

element_to_temperature_mapping ={
    Element.LAND.name: 25,
    Element.SEA.name: 20,
    Element.ICEBURG.name: -15,
    Element.FOREST.name: 20,
    Element.CITY.name: 27,
}

class CellParameters:
    def __init__(self, element, wind, is_cloudy, air_pollution = 0.08):
        self.element = element
        self.wind = wind
        self.is_cloudy = is_cloudy
        self.air_pollution = air_pollution
        self.temperature = element_to_temperature_mapping[element.name]
    
    def to_string(self):
        print(self.temperature)
