import requests, json
import serial
import adafruit_thermal_printer
from datetime import datetime, timedelta
from requests_html import HTMLSession
from printerTools import *

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
printer = ThermalPrinter(uart)

def printTest():
    printer.feed(2)
    printer.print("TEST")
    printer.feed(2)