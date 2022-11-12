from tkinter import *
from tkinter import messagebox
import tkinter as tk
import main.location as loc


class Monitor():

    def __init__(self):
        loc_getter = loc.Location()
        location = loc_getter.get_random_location()
        longitude, latitude = location.coords[0][0], location.coords[0][1]
        self.longitude = longitude
        self.latitude = latitude
        self.root = tk.Tk()

    def __quit__(self):
        self.root.destroy()
        
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
        position.pack(side=tk.BOTTOM)

        reset = tk.Button(self.root, text='Quit', background='White', command=self.__quit__)
        reset.pack(side=tk.RIGHT, pady=150)
        

        def __show_weather__():
            messagebox.showinfo("Weather Report")

        weather = tk.Button(self.root, text='Weather Report', background='White', command=__show_weather__)
        weather.pack(side=tk.LEFT)


        self.root.mainloop()
        

        
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





# import requests
# import datetime
# from time import strftime

# # Use Geolocation API to fetch long/lat of target location
# city = input("Enter the city: ")
# state = input("Enter the state: ")
# country = input("Enter the country: ")

# query_parts = []
# if len(city) > 0:
#     query_parts.append(city)

# if len(state) > 0:
#     query_parts.append(state)

# if len(country) > 0:
#     query_parts.append(country)

# query_string = ",".join(query_parts)

# url = "http://api.openweathermap.org/geo/1.0/direct?q=" + query_string + "&limit=3&appid={00faf35a94b60514362028e180e2aadd}"

# response = requests.request("GET", url)

# status_code = response.status_code

# if status_code != 200:
# 	print("Uh oh, there was a problem when accessing the Geolocation API. Please try again later")
# 	quit()

# results = response.json()

# target_location = None
# if len(results) > 1:

#     message = "There is more than 1 result for your query, please select an option from the list below."
#     for index, result in enumerate(results):
#         message += "\n Enter (" + str(index + 1) + ") for: " + result["name"] + ", " + result["state"] + ", " + result["country"]
#     message += "\n"

#     target_location_index = input(message)

#     try:
#         target_location_index = int(target_location_index)

#         if target_location_index < 1 or target_location_index > len(results):
#             raise Exception
#     except Exception:
#         print("Valid option not selected, defaulting to option 1")
#         target_location_index = 1

#     target_location = results[target_location_index - 1]
# else: 
#     target_location = results[0]

# longitude = target_location["lon"]
# latitude = target_location["lat"]

# # Now use 5 day weather forecast API to fetch weather data based on the returned long/lat coordinates
# print("Looking up weather data for " + target_location["name"] + ", " + target_location["state"] + ", " + target_location["country"] + " (with long/lat: " + str(longitude) + "/" + str(latitude) + ")")

# url = "https://api.openweathermap.org/data/2.5/forecast?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid={00faf35a94b60514362028e180e2aadd}&units=metric"

# response = requests.request("GET", url)

# status_code = response.status_code

# if status_code != 200:
# 	print("Uh oh, there was a problem when accessing the 5 day weather forecast API. Please try again later")
# 	quit()

# results = response.json()

# output = ""

# for result in results["list"]:

#     time = datetime.datetime.fromtimestamp(result["dt"]).strftime("%a %d %b %H:%M %p")
#     temperature = result["main"]["temp"]
#     weather = result["weather"][0]["description"]
    
#     output += time + " " + str(temperature) + " " + str(weather) + "\n"

# print(output)
