import requests
import datetime
from time import strftime

#Using longitude and latitude variables get weather data

class Weather:

    def __init__(self, longitude, latitude):
        self.lattitude = latitude
        self.longitude = longitude
        self.__url = "https://api.openweathermap.org/data/2.5/forecast?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid={00faf35a94b60514362028e180e2aadd}&units=metric"

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

        print(output)


