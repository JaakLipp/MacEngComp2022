import main.location as loc
import GUI
import ControlSystems.ControlSystem as cs

def main():

    weather = cs.WeatherSystem(51.5074, 0.1278, False)
    w = weather.get_weather()
    print(w)
    weather.reset()

    my_gui = GUI.Monitor()

    my_gui.display()    

if __name__ == main():
    main()