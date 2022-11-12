from tkinter import *
from tkinter import messagebox
import tkinter as tk
import main.location as loc
import ControlSystems.ControlSystem as cs

class Monitor():
    '''
    class for the main GUI of the program
    '''

    def __init__(self, longitude, latitude):

        #assign location data
        self.longitude = longitude
        self.latitude = latitude

        #initialize the display for tkinter
        self.root = tk.Tk()

        #initialize weather data
        self.weather = cs.WeatherSystem(self.longitude, self.latitude, True)
        self.w = self.weather.get_weather()

    def __get_new_weather__(self):
        self.weather = cs.WeatherSystem(self.longitude, self.latitude, True)
        self.w = self.weather.get_weather()
    
    def display(self):
        
        #initializes the background
        self.root.title("A Sailor's Best Friend")
        self.root.geometry('600x400')
        bg = PhotoImage(file = 'styles\Picture1.png')
        label1 = Label( self.root, image = bg)
        label1.place(x = 0,y = 0)

        #Title displaying what you will be looking at
        var = StringVar()
        label = Label(self.root, textvariable=var, background='Black', font=('bold', 20), fg='white')
        var.set("OCEAN MONITORING")
        label.pack()

        #displays your location data
        position = tk.Label(self.root, text='Latitude: ' + str(self.latitude) + ' Longitude: ' + str(self.longitude), background='White')
        position.pack(side=tk.TOP)
        
        
        def __show_weather__():
            #helper function to determine which weather output to display
            if self.w == None:
                messagebox.showerror("Weather Report",  "Error connecting to the satelite, attempting to show previous data")
                corr = self.weather.get_correction()
                if corr != "":
                    messagebox.showinfo("Weather Report", corr)
            elif self.weather.get_Hazard_Conditions == 'Hazard':
                 messagebox.showwarning("Weather Report", 'THUNDERSTORM APPROACHING, BEWARE' + self.w)
            else:
                self.weather.reset()
                self.__get_new_weather__()
                messagebox.showinfo("Weather Report", self.w)

        #weather button
        weather = tk.Button(self.root, text='Weather Report', background='White', command=__show_weather__, font=("Arial", 15))
        weather.pack(side=tk.BOTTOM)

        def __show_currents__():
            #helper function showing ocean current data
            messagebox.showinfo("Currents", "Here is where current data would go")

        #ocean current button
        currrent = tk.Button(self.root, text='Ocean Current Report', background='White', command=__show_currents__, font=("Arial", 15))
        currrent.pack(side=tk.BOTTOM)

        #reset button
        reset = tk.Button(self.root, text='Reset Weather Data', background='White', command=self.weather.reset, font=("Arial", 10))
        reset.pack(side=tk.BOTTOM)
        
        def __broadcast_SOS__():
            #SOS helper function
            messagebox.showwarning('SOS', 'Emergency Services notified of your position')
        
        #SOS button
        SOS = tk.Button(self.root, text='SOS', background='Red', command=__broadcast_SOS__, fg='White', font=("Arial", 20))
        SOS.pack(side=tk.TOP, anchor=NE)

        self.root.mainloop()
        