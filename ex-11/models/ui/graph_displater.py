import statistics
import matplotlib.pyplot as plt

class GraphDisplayer:
    def __init__(self, daily_temperature_avg, daily_air_pollution_avg):
        self.yearly_temperature_average = statistics.mean(daily_temperature_avg)
        self.yearly_temperature_std_dev = statistics.pstdev(daily_temperature_avg)
        self.yearly_air_pol_average = statistics.mean(daily_air_pollution_avg)
        self.yearly_ail_pol_std_dev = statistics.pstdev(daily_air_pollution_avg)

        self.normalized_temperatures = self.get_normalized_daily_temperature(daily_temperature_avg)  
        self.normalized_air_pollutions = self.get_normalized_daily_air_pol(daily_air_pollution_avg)
    
    def get_normalized_daily_temperature(self, daily_temperature_avg):
        normalized_temperatures = []

        for daily_temperature in daily_temperature_avg:
            normalized_temperatures.append((daily_temperature - self.yearly_temperature_average) / self.yearly_temperature_std_dev)
        
        return normalized_temperatures
    
    def get_normalized_daily_air_pol(self, daily_air_pollution_avg):
        normalized_air_pollutions = []

        for daily_air_pol in daily_air_pollution_avg:
            normalized_air_pollutions.append((daily_air_pol - self.yearly_air_pol_average) / self.yearly_ail_pol_std_dev)
        
        return normalized_air_pollutions

    def display_linear_graph(self):
        dates = list(range(1, 367))

        plt.plot(dates, self.normalized_temperatures, label='Temperature (°C)', marker='o')
        plt.plot(dates, self.normalized_air_pollutions, label='Air Pollution', marker='x')
        
        plt.xlabel('Date')
        plt.ylabel('Values')
        plt.title('Daily Average Temperature and Air Pollution Over the Year')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout() 
        
        plt.show()