# import required modules
import requests, json
import serial
import adafruit_thermal_printer
import datetime
from keys import *

def weatherPrint():

	uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=5000)
	ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
	printer = ThermalPrinter(uart)

	current_time = datetime.datetime.now()

	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	complete_url = base_url + "appid=" + API_KEY + "&units=imperial&q=14611" 
	response = requests.get(complete_url)

	weather = response.json()

	if weather["cod"] != "404":

		line0 = "###############################"
		line1 = " _ _ _         _   _           "
		line2 = "| | | |___ ___| |_| |_ ___ ___ "
		line3 = "| | | | -_| .'|  _|   | -_|  _|"
		line4 = "|_____|___|__,|_| |_|_|___|_| "

		printer.print(line0)
		printer.print(line1)
		printer.print(line2)
		printer.print(line3)
		printer.print(line4)
		printer.print(line0)

		printer.feed(2)

		printer.print("Today is " + current_time.strftime('%A') + ", " + str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year))
		printer.feed(1)
		printer.print("Today in " + weather['name'] + "\nthere will be a high of " + str(weather['main']['temp_max']) + "\nand a low of " + str(weather['main']['temp_min']) + "\nbut currently it's " + str(weather['main']['temp']) + "\nbut feels like " + str(weather['main']['feels_like']))
		printer.feed(1)
		printer.print("You can expect " + weather['weather'][0]['main'] + ",\nspecifically " + weather['weather'][0]['description'])
		printer.feed(5)

	else:
		printer.print(" City Not Found ")
		printer.feed(10)