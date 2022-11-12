import main.location as loc
import GUI
import ControlSystems.ControlSystem as cs

def main():

<<<<<<< HEAD
    # weather = cs.WeatherSystem(51.5074, 0.1278, False)
    # w = weather.get_weather()
    # print(w)
=======
    weather = cs.WeatherSystem(51.5074, 0.1278, False)
    w = weather.get_weather()
    print(w)
    weather.reset()

>>>>>>> 7cf49d02b84c6132c6b85201704eab377b9be3be
    my_gui = GUI.Monitor()

    my_gui.display()    

if __name__ == main():
    main()