from abc import ABC, abstractmethod
import requests
import datetime
from time import strftime

class ControlSystem(ABC):
    @abstractmethod
    def get_errors(self):
        pass
    
    @abstractmethod
    def get_damages(self):
        pass

    @abstractmethod
    def get_correction(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def validate_sensor(self):
        pass
    

class WeatherSystem(ControlSystem):
    def __init__(self, longitude, latitude):
        self.lattitude = latitude
        self.longitude = longitude
        self.__url = "https://api.openweathermap.org/data/2.5/forecast?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=00faf35a94b60514362028e180e2aadd&units=metric"

    def get_weather(self):
        response = requests.request("GET", self.__url)
        
        status_code = response.status_code
        if status_code != 200:
            print("Uh oh, there was a problem when accessing the 5 day weather forecast API. Please try again later")
            quit()
        results = response.json()
        output = "" 
        for result in results["list"]:

            time = datetime.datetime.fromtimestamp(result["dt"]).strftime("%a %d %b %H:%M %p")
            temperature = result["main"]["temp"]
            weather = result["weather"][0]["description"]
            
            output += time + " " + str(temperature) + " " + str(weather) + "\n"

        return output
    
    def get_errors(self):
        pass

    def get_damages(self):
        pass

    def get_correction(self):
        pass

    def reset(self):
        pass

    def validate_sensor(self):
        pass

    