# import required modules
import requests, json
import serial
import adafruit_thermal_printer
import datetime
from keys import *

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
printer = ThermalPrinter(uart)

current_time = datetime.datetime.now()

base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + API_KEY + "&units=imperial&q=14611" 
response = requests.get(complete_url)

weather = response.json()

if weather["cod"] != "404":

	printer.print("Today is " + current_time.strftime('%A') + ", " + str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year))
	printer.feed(5)
	printer.print("Today in " + weather['name'] + " there will be a high of " + str(weather['main']['temp_max']) + " and a low of " + str(weather['main']['temp_min']) + " + but currently it's " + str(weather['main']['temp']) + " but feels like " + str(weather['main']['feels_like']))
	printer.feed(5)
	printer.print("You can expect " + weather['weather'][0]['main'] + " + specifically " + weather['weather'][0]['description'])
	printer.feed(10)

else:
	printer.print(" City Not Found ")
	printer.feed(10)