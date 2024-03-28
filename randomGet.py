import random
import time
import requests, json
import serial
import adafruit_thermal_printer
from keys import *
from printerTools import *

def printQuote():
    # Quotes
    base_url = "https://api.api-ninjas.com/v1/quotes"
    response = requests.get(base_url, headers={'X-Api-Key':NINJA_API_KEY})
    quotes = response.json()

    if response.ok: 
        printer.print(center_text("Quotes"))
        printer.print("From " + quotes[0]['author'])
        printer.feed(1)
        printer.print(quotes[0]['quote'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

def printJokes():
    # Jokes
    base_url = "https://api.api-ninjas.com/v1/jokes?limit=1"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    jokes = response.json()

    if response.ok:
        printer.print(center_text("Jokes"))
        printer.print(jokes[0]['joke'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

def printDadJokes():
    # Dad Jokes
    base_url = "https://api.api-ninjas.com/v1/dadjokes?limit=1"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    dadjokes = response.json()

    if response.ok:
        printer.print(center_text("Dad Jokes"))
        printer.print(dadjokes[0]['joke'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

def printFacts():
    # Facts
    base_url = "https://api.api-ninjas.com/v1/facts?limit=1"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    facts = response.json()

    if response.ok:
        printer.print(center_text("Facts"))
        printer.print(facts[0]['fact'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

def printRiddles():
    # Riddles
    base_url = "https://api.api-ninjas.com/v1/riddles"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    riddle = response.json()

    if response.ok:
        printer.print(center_text("Riddles"))
        printer.print(riddle[0]['title'])
        printer.feed(2)

        printer.print(riddle[0]['question'])
        printer.feed(2)

        time.sleep(5)

        printer.print(riddle[0]['answer'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)

def printTrivia():
    # Trivia
    base_url = "https://api.api-ninjas.com/v1/trivia"
    response = requests.get(base_url, headers={'X-Api-Key': NINJA_API_KEY})
    trivia = response.json()

    if response.ok:
        printer.print(center_text("Trivia"))
        printer.print("The category is " + trivia[0]['category'])
        printer.feed(2)

        printer.print(trivia[0]['question'])
        printer.feed(2)

        time.sleep(5)

        printer.print(trivia[0]['answer'])
        printer.feed(2)

        printer.print("###############################")
        printer.feed(2)

    else:
        printer.print("Error fetching API")
        printer.feed(2)


def printRandom():
    uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
    printer = ThermalPrinter(uart)

    printer.print("###############################")
    printer.print(center_text(" ______             "))
    printer.print(center_text("|  ____|            "))
    printer.print(center_text("| |__  _   _  _ __  "))
    printer.print(center_text("|  __|| | | || '_ \ "))
    printer.print(center_text("| |   | |_| || | | |"))
    printer.print(center_text("|_|    \__,_||_| |_|"))
    printer.print("###############################")

    printer.feed(2)

    # Print Logic

    num = random.randRange(1, 6)

    if num == 1:
        printQuote()
    elif num == 2:
        printJokes()
    elif num == 3:
        printDadJokes()
    elif num == 4:
        printFacts()
    elif num == 5:
        printRiddles()
    elif num == 6:
        printTrivia()
    else:
        printer.print("ERROR")

    printer.print("###############################")
    printer.feed(4)