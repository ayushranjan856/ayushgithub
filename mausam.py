# import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# extract key from the
# configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url ="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_file="ayush"
file_a=ConfigParser()
file_a.read(api_file)
api_key=file_A["api_key"]["key"]

# explicit function to get
# weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']["country"]
        temp_kelvin = json['main']['temp']
        temp_celsius = (temp_kelvin - 273.15)*9/5+32
        weather1 = json['weather'][0]['main']
        result = [city, country, temp_kelvin,
                 temp_celsius, weather1]
        return result
    else:
        print("NO Content Found")


# explicit function to
# search city
def search():
    city = city.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3]) + "   Degree Celsius"
        weather1['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


# Driver Code
# create object
app = Tk()
# add title
app.title("Weather App")
app.config(background="black")
app.geometry("300x300")

# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text,fg="blue",font=("Arial",30,"bold"))
city_entry.pack()
search_btn = Button(app, text="Search Weather",
                    width=12, command=search)
Search_btn.pack()
location_lbl = Label(app, text="Location", font=('bold', 20))
location_lbl.pack()
temperature_label = Label(app, text="",font=("Arial",35,"bold"),bg="lightpink")
temperature_label.pack()
weather_l = Label(app, text="",font=("Arial",35,"bold"),bg="lightgreen")
weather_l.pack()
app.mainloop()