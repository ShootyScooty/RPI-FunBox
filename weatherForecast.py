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

	print(weather)

	line1 = "Today is ", current_time.strftime('%A'), ", ", current_time.month, " ", current_time.day, ", ", current_time.year
	line2 = "Today in ", weather['name'], " there will be a high of ", weather['main']['temp_max'], " and a low of ", weather['main']['temp_min'], ", but currently it's ", weather['main']['temp'], " but feels like ", weather['main']['feels_like']
	line3 = "You can expect ", weather['weather'][0]['main'], ", specifically ", weather['weather'][0]['description']

	printer.print(line1)
	printer.feed(5)
	printer.print(line2)
	printer.feed(5)
	printer.print(line3)
	printer.feed(10)

else:
	printer.print(" City Not Found ")
	printer.feed(10)