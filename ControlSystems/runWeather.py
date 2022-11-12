import ControlSystem as cs

def main():
    #runs the weather system, this is purely for testing
    weather = cs.WeatherSystem(51.5074, 0.1278)
    weather.get_weather()

if __name__ == "__main__":
    main()
