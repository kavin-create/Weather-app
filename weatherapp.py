import requests
from tkinter import *
from PIL import ImageTk,Image

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=+{}+&appid=da975419b2f50dccef36a3ec5c8b2301&units=metric"

def get_weather(city):
    result = requests.get(complete_api_link.format(city))
    api_data = result.json()

    if result:
        temperature = api_data['main']['temp']   
        weathericon = api_data['weather'][0]['icon']
        weather = api_data['weather'][0]['main']
        l= ((str(temperature)+u"\N{DEGREE SIGN}" + "C"),weathericon,weather)
        return l
    else: 
        weather_label.forget()
        weather_condition_image.forget()
        temperature_label.forget()
        error_label['text'] = 'Please enter a city name'
        return None

def search():
    city = city_entry_box.get()
    weather =  get_weather(city)

    if weather : 
        get_image(weather[1]+'.png')
        global weather_label
        global weather_condition_image
        global temperature_label
        error_label.forget()
        weather_label['text'] = "weather :" + weather[2]
        weather_condition_image.config(image = weather_img)
        temperature_label['text'] = "temp : "+weather[0] 

    else:
        
        weather_label.forget()
        weather_condition_image.forget()
        temperature_label.forget()
        error_label['text'] = 'Please enter a city name'

def get_image(image_name):
    global weather_img
    weather_img = ImageTk.PhotoImage(Image.open(("c:\\Main\\python_codes\\weatherapp\\weathericons\\{}").format(image_name)))

app = Tk()
app.title("Weather app")
app.geometry('400x400')
app.configure(background = 'skyblue1')
city_entry_box = Entry(app, width = 20)
city_entry_box.pack()
search_btn = Button(app, text = 'Search weather',bg = 'white', width = 12, command = search)
search_btn.pack()
temperature_label = Label(app,text = '' ,bg = 'skyblue1',font = ('bold',20))
temperature_label.pack()
weather_label = Label(app , text = '',bg = 'skyblue1')
weather_label.pack()
weather_condition_image = Label(app,bg = 'skyblue1')
weather_condition_image.pack()
error_label = Label(app,text = '',bg = 'skyblue1')
error_label.pack()
app.mainloop()
