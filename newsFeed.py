import requests, json
import serial
import adafruit_thermal_printer
from keys import *
from printerTools import *

def printNews():
    uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
    printer = ThermalPrinter(uart)

    base_url = "https://newsapi.org/v2/top-headlines?country=us&pageSize=5&"
    complete_url = base_url + "apiKey=" + NEWS_API_KEY
    response = requests.get(complete_url)

    print (complete_url)

    news = response.json()

    print(news['status'])

    if news['status'] != "ok":
    
        printer.print("###############################")
        printer.print(center_text(" _   _                         "))
        printer.print(center_text("| \ | |                        "))
        printer.print(center_text("|  \| |   ___  __      __  ___ "))
        printer.print(center_text("| . ` |  / _ \ \ \ /\ / / / __|"))
        printer.print(center_text("| |\  | |  __/  \ V  V /  \__ \\"))
        printer.print(center_text("|_| \_|  \___|   \_/\_/   |___/"))
        printer.print("###############################")

        printer.feed(2)

        for article in news['articles']:
            printer.print("From " + article['source']['name'])
            printer.feed(1)
            printer.print(article['title'])
            printer.feed(1)
            printer.print(article['description'])
            printer.feed(1)
            printer.print("Published " + article['publishedAt'])
            printer.feed(2)

        printer.print("###############################")
        printer.feed(4)

    else:
        printer.print("Error fetching news API")
        printer.feed(4)
