import main.location as loc
from weather.weather import Weather

def main():

    loc_getter = loc.Location(180,180,-180,-180)

    location = loc_getter.get_random_location()
    print("Latitude: " + str(location.coords[0][0]) + ' Longitude: ' + str(location.coords[0][1]))
    w = Weather(location.coords[0][0], location.coords[0][1])
    w.get_weather()


if __name__ == main():
    main()
