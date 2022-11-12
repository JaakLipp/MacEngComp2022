import main.location as loc
from ControlSystems.weather import Weather
# from GUI import *
import GUI

loc_getter = loc.Location(180,180,-180,-180)
location = []
longitude, latitude = 0, 0


def main():
    my_gui = GUI.Monitor()

    my_gui.display()

    # print("Latitude: " + str(location.coords[0][0]) + ' Longitude: ' + str(location.coords[0][1]))
    # w = Weather(longitude, latitude)
    # w.get_weather()


if __name__ == main():
    main()
