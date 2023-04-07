# import required modules
import requests, json
import serial
import adafruit_thermal_printer
import datetime

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
printer = ThermalPrinter(uart)

current_time = datetime.now()

api_key = "Your_API_Key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&units=imperial&q=14611" 
response = requests.get(complete_url)

weather = response.json()

if weather["cod"] != "404":

	printer.print("Today is " + current_time.weekday + ", " + current_time.month + " " + current_time.day + ", " + current_time.year)
	printer.feed(5)
	printer.print("Today in " + weather['sys'].name + " there will be a high of " + weather['main'].temp_max + " and a low of " + weather['main'].temp_min + ", but currently it's " + weather['main'].temp + " but feels like " + weather['main'].feels_like)
	printer.feed(5)
	printer.print("You can expect " + weather['weather'][0].main + ", specifically " + weather['weather'][0].description)
	printer.feed(10)

else:
	printer.print(" City Not Found ")
	printer.feed(10)