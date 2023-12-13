from datetime import datetime, timedelta
from requests_html import HTMLSession
import requests, json
import serial
import adafruit_thermal_printer

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
printer = ThermalPrinter(uart)


monems = "https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1077"
monfire = "https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1811"
henfire = "https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1654"
ritpub = "https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=3070"
ritamb = "https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1894"
ritops = "https://clearcutradio.app/api/v1/calls?system=very-bad&talkgroup=100"

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

    message = "Monroe County 911 Events:\n\n"

    with response as r:
        items = r.html.find("item", first=False)

        for item in items:        

            title = item.find('title', first=True).text

            if not title.startswith("PARKING INCIDENT"):
                description = item.find('description', first=True).text

                pubdate = item.find('pubDate', first=True).text

                message += str(title + " | " + description + " | " + pubdate + "\n")

    # n = 1994 # chunk length
    # chunks = [out[i:i+n] for i in range(0, len(out), n)]

    # for c in chunks:
    #     printer.print(c)
    #     printer.feed(1)

    response = get_source_clearcut(monems)
    message += "\nRIT EMS Call Transcripts:\n\n"

    for data in response:
        if (data is not None and data['transcript'] is not None and data['transcript']['text'] is not None):
            timestamp = datetime.fromtimestamp(data['startTime']) - timedelta(hours = 4)
            text = data['transcript']['text']

            # Get all calls within num range with matching keywords
            if ("RIT" in text or "6359" in text or "6-3-5-9" in text or "Defib 63" in text or "DEFIB 63" in text or "defib 63" in text):
                message += str(timestamp) + " | " + text + "\n\n"

    response = get_source_clearcut(henfire)
    message += "\n\nRIT Fire Related Call Transcripts:\n\n"

    for data in response:
        if (data is not None and data['transcript'] is not None and data['transcript']['text'] is not None):
            timestamp = datetime.fromtimestamp(data['startTime']) - timedelta(hours = 4)
            text = data['transcript']['text']

            # Get all calls within num range with matching keywords
            if ("RIT" in text):
                message += str(timestamp) + " | " + text + "\n\n"

    printer.print(message)
    printer.feed(2)