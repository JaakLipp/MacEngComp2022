import main.location as loc
from weather.weather import Weather
import GUI

loc_getter = loc.Location(180,180,-180,-180)
location = []
longitude, latitude = 0, 0


def main():
    if location == []:
        location = loc_getter.get_random_location()
        longitude, latitude = location.coords[0][0], location.coords[0][1]

    GUI()

    # print("Latitude: " + str(location.coords[0][0]) + ' Longitude: ' + str(location.coords[0][1]))
    # w = Weather(longitude, latitude)
    # w.get_weather()


if __name__ == main():
    main()
