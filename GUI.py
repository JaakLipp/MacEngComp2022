from tkinter import *
from tkinter import messagebox
import tkinter as tk
import main.location as loc
import ControlSystems.ControlSystem as cs

class Monitor():

    def __init__(self):
        loc_getter = loc.Location()
        location = loc_getter.get_random_location()
        longitude, latitude = location.coords[0][0], location.coords[0][1]
        self.longitude = longitude
        self.latitude = latitude
        self.root = tk.Tk()

        
    def display(self):
        
        self.root.title("Ocean Monitor")
        self.root.geometry('600x400')
        bg = PhotoImage(file = 'styles\Picture1.png')
        label1 = Label( self.root, image = bg)
        label1.place(x = 0,y = 0)


        var = StringVar()
        label = Label(self.root, textvariable=var, background='White')
        var.set("OCEAN MONITORING")
        label.pack()

        position = tk.Label(self.root, text='Latitude: ' + str(self.latitude) + ' Longitude: ' + str(self.longitude), background='White')
        position.pack(side=tk.TOP)
        

        def __show_weather__():

            weather = cs.WeatherSystem(longitude=self.longitude, latitude=self.latitude)
            w = weather.get_weather()
            if w == "Uh oh, there was a problem when accessing the 5 day weather forecast API. Please try again later":
                messagebox.showerror("Weather Report", w)
            else:
                messagebox.showinfo("Weather Report", w)

        weather = tk.Button(self.root, text='Weather Report', background='White', command=__show_weather__, font=("Arial", 15))
        weather.pack(side=tk.BOTTOM)

        def __show_currents__():
            messagebox.showinfo("Currents", "Here is where current data would go")

        weather = tk.Button(self.root, text='Ocean Current Report', background='White', command=__show_currents__, font=("Arial", 15))
        weather.pack(side=tk.BOTTOM)


        def __broadcast_SOS__():
            messagebox.showwarning('SOS', 'Emergency Services notified of your position')
        
        SOS = tk.Button(self.root, text='SOS', background='Red', command=__broadcast_SOS__, fg='White', font=("Arial", 20))
        SOS.pack(side=tk.TOP, anchor=NE)

        self.root.mainloop()
        