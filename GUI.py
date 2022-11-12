from tkinter import *
import tkinter as tk
from tkinter import messagebox
import main.location as loc
from weather.weather import Weather

class Monitor():

    def __init__(self):
        loc_getter = loc.Location(180,180,-180,-180)
        location = loc_getter.get_random_location()
        longitude, latitude = location.coords[0][0], location.coords[0][1]
        self.longitude = longitude
        self.latitude = latitude

    def display(self):
        root = tk.Tk()
        root.title("Ocean Monitor")
        root.geometry('600x400')
        bg = PhotoImage(file = 'styles\Picture1.png')
        label1 = Label( root, image = bg)
        label1.place(x = 0,y = 0)


        var = StringVar()
        label = Label(root, textvariable=var, background='White')
        var.set("OCEAN MONITORING")
        label.pack()



        position = tk.Label(root, text='Latitude: ' + str(self.latitude) + ' Longitude: ' + str(self.longitude), background='White')
        position.pack(side=tk.BOTTOM)

        root.mainloop()
        




# def weather_data():
#     messagebox.showinfo("Number of Votes for Pineapple on Pizza: ", "Number of Votes for Pineapple on Pizza: " +str(votes[0]))
# b = Button(root, text ="Weather Data",  height=100, width=200, command = )
# b.pack()

# var6 = StringVar()
# label6 = Label(root, textvariable=var6, bg='#B9FF98')
# var6.set("")
# label6.pack(anchor=tk.W)

# var2 = StringVar()
# label2 = Label(root, textvariable=var2)
# var2.set("Pronouced Jeff Union")
# label2.pack()

# def pronouncedJeff():
#     messagebox.showinfo("Number of Votes for Pronounced Jeff Union: ", "Number of Votes for Pronounced Jeff Union: " + str(votes[1]))
# b2 = Button(root, text ="PronouncedJeffUnion", image=jeff_btn, height=100, width=200, command = pronouncedJeff)
# b2.pack()

# var4 = StringVar()
# label4 = Label(root, textvariable=var4)
# var4.set("Click on each party to \n review their votes")
# label4.pack(anchor=tk.W)

# var3 = StringVar()
# label3 = Label(root, textvariable=var3)
# var3.set("Socks and Crocs Reform")
# label3.pack()

# def socksandCrocsReform():
#    messagebox.showinfo("Number of Votes for Socks and Crocs Reform League: ", "Number of Votes for Socks and Crocs Reform League: " + str(votes[2]))
# b3 = Button(root, text ="SocksandCrocks", image=croc_btn, height=100, width=200, command = socksandCrocsReform)
# b3.pack()





