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
    def __init__(self, longitude, latitude, connection):
        self.lattitude = latitude
        self.longitude = longitude
        self.connection = True
        self.__url = "https://api.openweathermap.org/data/2.5/forecast?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=00faf35a94b60514362028e180e2aadd&units=metric"

    def get_weather(self):
        if self.connection:
            response = requests.request("GET", self.__url)
            
            status_code = response.status_code
            if status_code != 200:
                self.get_errors("Uh oh, there was a problem when connecting to the satellite. Please try again later")
                quit()
            results = response.json()
            output = "" 
            for result in results["list"]:

                time = datetime.datetime.fromtimestamp(result["dt"]).strftime("%a %d %b %H:%M %p")
                temperature = result["main"]["temp"]
                weather = result["weather"][0]["description"]
                
                output += time + " " + str(temperature) + " " + str(weather) + "\n"
            self.write_to_file(output)

            return output
        else:
            return self.get_correction()
    
    def get_errors(self, message):
        print(message)

    def get_damages(self):
        pass

    def get_correction(self):
        file = open("PastData.txt", "r")
        data = file.read()
        file.close()
        return data

    def reset(self):
        pass

    def validate_sensor(self):
        pass

    def write_to_file(self, data):
        file = open("PastData.txt", "w")
        file.write(data)
        file.close()
    
    