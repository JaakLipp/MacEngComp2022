import main.location as loc
from weather.weather import Weather
# from GUI import *
import GUI

def main():
    my_gui = GUI.Monitor()

    my_gui.display()

    # print("Latitude: " + str(location.coords[0][0]) + ' Longitude: ' + str(location.coords[0][1]))
    # w = Weather(longitude, latitude)
    # w.get_weather()


if __name__ == main():
    main()
