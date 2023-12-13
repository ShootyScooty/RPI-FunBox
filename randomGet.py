import requests, json
import serial
import adafruit_thermal_printer
from keys import *
from printerTools import *

def printRandom():
    uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
    printer = ThermalPrinter(uart)

    printer.print("###############################")
    printer.print(center_text(" _____                 _                 "))
    printer.print(center_text("|  __ \               | |                "))
    printer.print(center_text("| |__) |__ _ _ __   __| | ___  _ __ ___  "))
    printer.print(center_text("|  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \ "))
    printer.print(center_text("| | \ \ (_| | | | | (_| | (_) | | | | | |"))
    printer.print(center_text("|_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_|"))
    printer.print("###############################")

    printer.feed(2)

    # Quotes
    base_url = "https://api.api-ninjas.com/v1/quotes"
    response = requests.get(base_url, headers={'X-Api-Key':NINJA_API_KEY})
    quotes = response.json()

    if response.ok(): 
        printer.print("From " + quotes['author'])
        printer.feed(1)
        printer.print(quotes['quote'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

    # Jokes
    base_url = "https://api.api-ninjas.com/v1/jokes?limit=1"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    jokes = response.json()

    if response.ok():
        printer.print(jokes['joke'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

    # Dad Jokes
    base_url = "https://api.api-ninjas.com/v1/dadjokes?limit=1"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    dadjokes = response.json()

    if response.ok():
        printer.print(dadjokes['joke'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

    # Facts
    base_url = "https://api.api-ninjas.com/v1/facts?limit=1"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    facts = response.json()

    if response.ok():
        printer.print(facts['fact'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

    # Riddles
    base_url = "https://api.api-ninjas.com/v1/riddles"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    riddle = response.json()

    if response.ok():
        printer.print(riddle['title'])
        printer.feed(2)

        printer.print(riddle['question'])
        printer.feed(2)

        printer.print(riddle['answer'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

    # Trivia
    base_url = "https://api.api-ninjas.com/v1/trivia"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    trivia = response.json()

    if response.ok():
        printer.print("The category is " + trivia['category'])
        printer.feed(2)

        printer.print(trivia['question'])
        printer.feed(2)

        printer.print(trivia['answer'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

    printer.print("###############################")
    printer.feed(4)