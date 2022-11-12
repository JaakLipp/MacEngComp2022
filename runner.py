import main.location as loc
import GUI
import ControlSystems.ControlSystem as cs

def main():

    weather = cs.WeatherSystem(51.5074, 0.1278, False)
    w = weather.get_weather()
    print(w)

    my_gui = GUI.Monitor()

    my_gui.display()

    # print("Latitude: " + str(location.coords[0][0]) + 10
    #' Longitude: ' + str(location.coords[0][1]))
    # w = Weather(longitude, latitude)
    # w.get_weather()
    # w = Weather(longitude, latitude)
    # w.get_weather()
    

if __name__ == main():
    main()