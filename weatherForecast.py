# import required modules
import requests, json
import serial
import adafruit_thermal_printer
import datetime
from keys import *

def weatherPrint():

	uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
	ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
	printer = ThermalPrinter(uart)

	current_time = datetime.datetime.now()

	base_url = "http://api.openweathermap.org/data/2.5/weather?lat=43.144&lon=-77.6406&"
	complete_url = base_url + "appid=" + API_KEY + "&units=imperial"
	response = requests.get(complete_url)

	weather = response.json()

	base_url = "http://api.openweathermap.org/data/2.5/forecast?lat=43.144&lon=-77.6406&"
	complete_url = base_url + "appid=" + API_KEY + "&units=imperial"
	response = requests.get(complete_url)

	future = response.json()

	if weather['cod'] != "404":

		name = weather['name']
		max = (weather['main']['temp_max'])
		min = (weather['main']['temp_min'])
		cur = (weather['main']['temp'])
		feel = (weather['main']['feels_like'])

		printer.print("###############################")
		printer.print(" _ _ _         _   _           ")
		printer.print("| | | |___ ___| |_| |_ ___ ___ ")
		printer.print("| | | | -_| .'|  _|   | -_|  _|")
		printer.print("|_____|___|__,|_| |_|_|___|_| ")
		printer.print("###############################")

		printer.feed(2)

		printer.print("Today is " + current_time.strftime('%A') + ", " + str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year))
		printer.feed(1)
		printer.print("Today in " + name + "\nthere will be a high of " + str(max) + "F\nand a low of " + str(min) + "F\n")
		printer.feed(1)
		printer.print("Currently it's " + str(cur) + "F\nbut feels like " + str(feel) + "F")
		printer.feed(1)
		printer.print("The humidity is " + str(weather['main']['humidity']) + "%,\nthe pressure is " + str(weather['main']['pressure']) + " hPa,\nthe visibility is " + str(weather['visibility']) + " meters,\nand the wind speed is " + str(weather['wind']['speed']) + " mph")
		printer.feed(1)
		printer.print("You can expect " + weather['weather'][0]['main'] + "\nspecifically, " + weather['weather'][0]['description'])
		
		printer.feed(2)

		# if future['cod'] != "404":

		# 	future = future['list']
			
		# 	printer.print("##########--5 Day--############")

		# 	for x in future:
		# 		printer.print("On " + x['dt_txt'] + "\nthere will be a high of " + str(x['main']['temp_max']) + "F\nand a low of " + str(x['main']['temp_min']) + "F")
		# 		printer.feed(1)
		# 		printer.print("You can expect " + x['weather'][0]['main'] + ",\nspecifically " + x['weather'][0]['description'])

		# 	printer.print("###############################")
		# else:
		# 	printer.print("###############################")

		printer.print("###############################")

	else:
		printer.print(" City Not Found ")
		printer.feed(10)