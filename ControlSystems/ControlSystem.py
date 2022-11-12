from abc import ABC, abstractmethod
import requests
import datetime
from time import strftime

#abstract class for all control systems
#defines the class structure for all control systems
class ControlSystem(ABC):
    @abstractmethod
    def get_errors(self):
        pass
    
    @abstractmethod
    def get_Hazard_Conditions(self):
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

    
    
#class for weather, inherits from ControlSystem
class WeatherSystem(ControlSystem):
    def __init__(self, longitude, latitude, connection):
        #variables to connect to the API
        self.lattitude = latitude
        self.longitude = longitude
        #connection is a boolean to check if the connection is working
        self.connection = connection
        #output the data
        self.output = ""
        #url to connect to the API
        self.__url = "https://api.openweathermap.org/data/2.5/forecast?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=00faf35a94b60514362028e180e2aadd&units=metric"
    
    def get_weather(self):
        #if the connection is working
        if self.connection:
            #get the data from the API
            response = requests.request("GET", self.__url)
            #get the status code
            status_code = response.status_code
            #if the status code is 200 meaning having trouble connecting to the API..."Satellite is down"
            if status_code != 200:
                self.get_errors("Uh oh, there was a problem when connecting to the satellite. Please try again later")
                quit()
            #get response in json format
            results = response.json()
            output = "" 
            #extract the information from the json file and format it
            for result in results["list"]:
                #get the date and time
                time = datetime.datetime.fromtimestamp(result["dt"]).strftime("%a %d %b %H:%M %p")
                #get the temperature
                temperature = result["main"]["temp"]
                #get the weather description
                weather = result["weather"][0]["description"]
                #concatenate to the output
                output += time + " " + str(temperature) + " " + str(weather) + "\n"
            #write the output to the file to store the data
            self.write_to_file(output)
            self.output = output
            #return the output
            return output
        #if the connection is not working, we want to access the past data stored in the file
        #even though its not the most recent data, it is better than nothing to guide the user
        else:
            return self.get_correction()
    #method to get errors
    def get_errors(self, message):
        print(message)

    #method to get the hazard conditions
    def get_Hazard_Conditions(self):
        #if a hazard condtion is met...return a message
        if('thunderstorm' in self.output):
            return "Thunderstorms are expected in the area, please re route to a safe location"
        else:
            return "No Hazard Conditions"

    #method to get the past data from the file
    def get_correction(self):
        #read all data from file using with open
        self.get_errors("Power Faliure...loading past data results")
        with open("PastData.txt", "r") as file:
            data = file.read()
        return data

    #reset the data in the file
    def reset(self):
        file_to_delete = open("PastData.txt",'w')
        file_to_delete.close()

    #not applicable for weather
    def validate_sensor(self):
        pass

    #method to write the data to the file
    def write_to_file(self, data):
        #add data to file using with open
        with open("PastData.txt", "a") as file:
            file.write(data)
    
    