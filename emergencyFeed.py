import time
import requests, json
import serial
import adafruit_thermal_printer
from datetime import datetime, timedelta
from requests_html import HTMLSession
from printerTools import *

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
printer = ThermalPrinter(uart)

ts_now = int(time.time())

ts_24 = ts_now - (24 * 60 * 60)

monems = "https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1077" + "&before_ts=" + str(ts_now) + "&after_ts=" + str(ts_24)
henfire = "https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1654" + "&before_ts=" + str(ts_now) + "&after_ts=" + str(ts_24)

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

def get_source_rss():
    try:
        session = HTMLSession()
        response = session.get("https://www.monroecounty.gov/incidents911.rss")
        return response

    except requests.exceptions.RequestException as e:
        print(e)    

# ------------------ End RSS Functions ------------------
        
def matching(sentence, words):
    # Convert both the sentence and words to lowercase for case-insensitive comparison
    lowercase_sentence = sentence.lower()
    lowercase_words = [word.lower() for word in words]

    # Check if any word in the array is present in the sentence
    return any(word in lowercase_sentence for word in lowercase_words)

def printEmergency():

    printer.print("###############################")
    printer.print(center_text("  ___    __   __ "))
    printer.print(center_text(" / _ \  /_ | /_ |"))
    printer.print(center_text("| (_) |  | |  | |"))
    printer.print(center_text(" \__, |  | |  | |"))
    printer.print(center_text("   / /   | |  | |"))
    printer.print(center_text("  /_/    |_|  |_|"))
    printer.print("###############################")

    events = 0

    keywords = ["RIT", "rit", "R I T", "r i t", "6359", "6 3 5 9", "6-3-5-9", "Defib 63", "DEFIB 63", "defib 63", "Defib 6-3", "DEFIB 6-3", "defib 6-3", "601", "6 0 1", "Andrews", "Andrews Memorial", "Andrews Memorial Drive", "Lomb", "Lomb Memorial", "Lomb Memorial Drive", "Lowenthall", "Perkins", "Riverknoll", "University Commons", "Wiltsie", "Greenleaf", "Greenleaf Court", "Gleason", "Reynolds", "Kimball", "Farnum", "Charters"]

    response = get_source_clearcut(monems)

    printer.print("\nRIT EMS Call Transcripts:")
    printer.feed(1)

    for data in response:
        if (data is not None and data['transcript'] is not None and data['transcript']['text'] is not None):
            timestamp = datetime.fromtimestamp(data['startTime']) - timedelta(hours = 4)
            text = data['transcript']['text']

            if (matching(text, keywords)):
                events += 1
                printer.print(str(timestamp) + " | " + text)
                printer.feed(1)

    response = get_source_clearcut(henfire)

    printer.print("\n\nRIT Fire Related Call Transcripts:\n\n")
    printer.feed(1)

    for data in response:
        if (data is not None and data['transcript'] is not None and data['transcript']['text'] is not None):
            timestamp = datetime.fromtimestamp(data['startTime']) - timedelta(hours = 4)
            text = data['transcript']['text']

            if (matching(text, keywords)):
               printer.print(str(timestamp) + " | " + text)
               printer.feed(1)

    if events == 0:
        response = get_source_rss()
        printer.print("Monroe County 911 Events:")
        printer.feed(1)

        with response as r:
            items = r.html.find("item", first=False)

            for item in items:        

                title = item.find('title', first=True).text

                if not title.startswith("PARKING INCIDENT") and events < 11:
                    description = item.find('description', first=True).text

                    pubdate = item.find('pubDate', first=True).text

                    printer.print(str(title + " | " + description + " | " + pubdate))
                    printer.feed(1)

                    events += 1

    printer.print("###############################")
    printer.feed(4)