from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import requests
import json

def fetch_weather():
    city = city_name.get()
    api_key = '{YOUR_API_KEY}'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    data = response.json()
    print(data)  # Print the entire JSON response for debugging
    temperature = data['main']['temp']
    description = data['weather'][0]['main']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    visibility = data['visibility']
    visibility_km = visibility / 1000  # Convert visibility from meters to kilometers
    print(feels_like)
    temperature_label.config(text=f"{temperature} °C")
    discription_label.config(text=f"{description}")
    feels_like_value.config(text=f"{feels_like}°")
    humidity_value.config(text=f"{humidity} %")
    wind_speed_value.config(text=f"{wind_speed} mi/h")
    pressure_value.config(text=f"{pressure} hPa")
    visibility_value.config(text=f"{visibility_km} km")


win = Tk()
win.title("Weather")

# Configure window
win.configure(bg='#164f81')
win.geometry("500x600")
win.resizable(False, False)

# Set icon
logo_img = PhotoImage(file="Images/weather-app.png")
win.iconphoto(False, logo_img)

# Weather App label
name_label = Label(win, text="Weather App", font=("Times New Roman", 35, "bold"), fg='white', bg='#164f81')
name_label.place(x=25, y=50, height=50, width=450)

# Read city data from JSON file
with open("data.json", "r") as f:
    city_data = json.load(f)

city_name = StringVar()
# Extract city names from the list of dictionaries
city_names = [city["name"] for city in city_data]

# Combobox for selecting city
com_box = ttk.Combobox(win, values=city_names, font=("Times New Roman", 15), textvariable=city_name)
com_box.place(x=25, y=120, height=30, width=450)

# Search button
button = Button(win, text="Search", font=("Times New Roman", 15), command=fetch_weather)
button.place(y=160, height=50, width=100, x=200)

# Label to display weather information
temperature_label = Label(win, text="", font=("Times New Roman", 25,"bold"), bg='#164f81',fg='white')
temperature_label.place(x=25, y=240, height=30, width=450)

#Label to display weather discription information
discription_label = Label(win, text="", font=("Times New Roman", 15), bg='#164f81',fg='white')
discription_label.place(x=25, y=270, height=30, width=450)

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Canvas to draw Feels Like rounded rectangle
feels_like_canvas = Canvas(win, bg='#164f81', highlightthickness=0)
feels_like_canvas.place(x=50, y=310, width=120, height=100)

# Feels Like icon
feels_like_icon_img = Image.open("Images/feels-like.png")
resized_feels_like_icon_img = feels_like_icon_img.resize((25, 25))
feels_like_icon = ImageTk.PhotoImage(resized_feels_like_icon_img)
feels_like_icon_label = Label(win, image=feels_like_icon, bg='#214562')
feels_like_icon_label.place(x=97, y=312)

# Draw Feels Like rounded rectangle on Canvas
round_rectangle(feels_like_canvas, 0, 0, 120, 100, radius=20, fill="#214562")

# Place labels or other widgets on the feels_like_canvas
feels_like_label1 = Label(win, text="Feels Like", font=("Time New Roman", 12), bg="#214562", fg='white')
feels_like_label1.place(x=70, y=340)
feels_like_value = Label(feels_like_canvas, text="", font=("Time New Roman", 13,"bold"), bg="#214562", fg='white')
feels_like_value.place(x=26, y=52)

# Canvas to draw Humidity rounded rectangle
humidity_canvas = Canvas(win, bg='#164f81', highlightthickness=0)
humidity_canvas.place(x=200, y=310, width=120, height=100)

# Humidity icon
humidity_icon_img = Image.open("Images/humidity.png")
resized_humidity_icon_img = humidity_icon_img.resize((25, 25))
humidity_icon = ImageTk.PhotoImage(resized_humidity_icon_img)
humidity_icon_label = Label(win, image=humidity_icon, bg='#214562')
humidity_icon_label.place(x=245, y=312)

# Draw Visibility rounded rectangle on Canvas
round_rectangle(humidity_canvas, 0, 0, 120, 100, radius=20, fill="#214562")

# Place labels or other widgets on the humidity_canvas
humidity_label1 = Label(win, text="Humidity", font=("Time New Roman", 12), bg="#214562", fg='white')
humidity_label1.place(x=220, y=340)
humidity_value = Label(humidity_canvas, text="", font=("Time New Roman", 13,"bold"), bg="#214562", fg='white')
humidity_value.place(x=30, y=52)

# Canvas to draw Wind Speed rounded rectangle
wind_speed_canvas = Canvas(win, bg='#164f81', highlightthickness=0)
wind_speed_canvas.place(x=350, y=310, width=120, height=100)

# Wind Speed icon
wind_speed_icon_img = Image.open("Images/wind-speed.png")
resized_wind_speed_icon_img = wind_speed_icon_img.resize((25, 25))
wind_speed_icon = ImageTk.PhotoImage(resized_wind_speed_icon_img)
wind_speed_icon_label = Label(win, image=wind_speed_icon, bg='#214562')
wind_speed_icon_label.place(x=400, y=312)

# Draw Visibility rounded rectangle on Canvas
round_rectangle(wind_speed_canvas, 0, 0, 120, 100, radius=20, fill="#214562")

# Place labels or other widgets on the wind_speed_canvas
wind_speed_label1 = Label(win, text="Wind Speed", font=("Time New Roman", 12), bg="#214562", fg='white')
wind_speed_label1.place(x=360, y=340)
wind_speed_value = Label(wind_speed_canvas, text="", font=("Time New Roman", 13,"bold"), bg="#214562", fg='white')
wind_speed_value.place(x=13, y=52)

# Canvas to draw Pressure rounded rectangle
pressure_canvas = Canvas(win, bg='#164f81', highlightthickness=0)
pressure_canvas.place(x=120, y=430, width=120, height=100)

# Pressure icon
pressure_icon_img = Image.open("Images/air-pressure.png")
resized_pressure_icon_img = pressure_icon_img.resize((25, 25))
pressure_icon = ImageTk.PhotoImage(resized_pressure_icon_img)
pressure_icon_label = Label(win, image=pressure_icon, bg='#214562')
pressure_icon_label.place(x=170, y=435)

# Draw Visibility rounded rectangle on Canvas
round_rectangle(pressure_canvas, 0, 0, 120, 100, radius=20, fill="#214562")

# Place labels or other widgets on the pressure_canvas
pressure_label1 = Label(win, text="Air Pressure", font=("Time New Roman", 12), bg="#214562", fg='white')
pressure_label1.place(x=130, y=460)
pressure_value = Label(pressure_canvas, text="", font=("Time New Roman", 13,"bold"), bg="#214562", fg='white')
pressure_value.place(x=13, y=52)

# Canvas to draw Visibility rounded rectangle
visibility_canvas = Canvas(win, bg='#164f81', highlightthickness=0)
visibility_canvas.place(x=270, y=430, width=120, height=100)

# Visibility icon
visibility_icon_img = Image.open("Images/visibility.png")
resized_visibility_icon_img = visibility_icon_img.resize((25, 25))
visibility_icon = ImageTk.PhotoImage(resized_visibility_icon_img)
visibility_icon_label = Label(win, image=visibility_icon, bg='#214562')
visibility_icon_label.place(x=315, y=435)

# Draw Visibility rounded rectangle on Canvas
round_rectangle(visibility_canvas, 0, 0, 120, 100, radius=20, fill="#214562")

# Place labels or other widgets on the visibility_canvas
visibility_label1 = Label(win, text="Visibility", font=("Time New Roman", 12), bg="#214562", fg='white')
visibility_label1.place(x=295, y=460)
visibility_value = Label(visibility_canvas, text="", font=("Time New Roman", 13,"bold"), bg="#214562", fg='white')
visibility_value.place(x=15, y=52)


win.mainloop()
