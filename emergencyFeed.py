import requests, json
import serial
import adafruit_thermal_printer
from datetime import datetime, timedelta
from requests_html import HTMLSession
from printerTools import *

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
printer = ThermalPrinter(uart)

monems = "https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1077"
henfire = "https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1654"

# ------------------ ClearCut Functions ------------------

def get_source_clearcut(url):
    try:
        data = requests.get(url=url)
        response = data.json()
        return response

    except requests.exceptions.RequestException as e:
        print(e)

# ------------------ End ClearCut Functions ------------------

# ------------------ RSS Functions ------------------

def get_source():
    try:
        session = HTMLSession()
        response = session.get("https://www.monroecounty.gov/incidents911.rss")
        return response

    except requests.exceptions.RequestException as e:
        print(e)    

# ------------------ End RSS Functions ------------------

def printEmergency():
    response = get_source()

    printer.print("###############################")
    printer.print(center_text("  ___    __   __ "))
    printer.print(center_text(" / _ \  /_ | /_ |"))
    printer.print(center_text("| (_) |  | |  | |"))
    printer.print(center_text(" \__, |  | |  | |"))
    printer.print(center_text("   / /   | |  | |"))
    printer.print(center_text("  /_/    |_|  |_|"))
    printer.print("###############################")

    # printer.print(center_text("  ___  __ __ "))
    # printer.print(center_text(" / _ \/_ /_ |"))
    # printer.print(center_text("| (_) || || |"))
    # printer.print(center_text(" \__, || || |"))
    # printer.print(center_text("   / / | || |"))
    # printer.print(center_text("  /_/  |_||_|"))

    printer.print("Monroe County 911 Events:")
    printer.feed(1)

    with response as r:
        items = r.html.find("item", first=False)

        for item in items:        

            title = item.find('title', first=True).text

            if not title.startswith("PARKING INCIDENT"):
                description = item.find('description', first=True).text

                pubdate = item.find('pubDate', first=True).text

                printer.print(str(title + " | " + description + " | " + pubdate))
                printer.feed(1)

    response = get_source_clearcut(monems)

    printer.print("\nRIT EMS Call Transcripts:")
    printer.feed(1)

    for data in response:
        if (data is not None and data['transcript'] is not None and data['transcript']['text'] is not None):
            timestamp = datetime.fromtimestamp(data['startTime']) - timedelta(hours = 4)
            text = data['transcript']['text']

            # Get all calls within num range with matching keywords
            if ("RIT" in text or "6359" in text or "6-3-5-9" in text or "Defib 63" in text or "DEFIB 63" in text or "defib 63" in text):
                printer.print(str(timestamp) + " | " + text)
                printer.feed(1)

    response = get_source_clearcut(henfire)

    printer.print("\n\nRIT Fire Related Call Transcripts:\n\n")
    printer.feed(1)

    for data in response:
        if (data is not None and data['transcript'] is not None and data['transcript']['text'] is not None):
            timestamp = datetime.fromtimestamp(data['startTime']) - timedelta(hours = 4)
            text = data['transcript']['text']

            # Get all calls within num range with matching keywords
            if ("RIT" in text):
               printer.print(str(timestamp) + " | " + text)
               printer.feed(1)

    printer.print("###############################")
    printer.feed(4)