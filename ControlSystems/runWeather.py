import ControlSystem as cs

def main():
    #runs the weather system
    weather = cs.WeatherSystem(51.5074, 0.1278)
    weather.get_weather()

if __name__ == "__main__":
    main()
