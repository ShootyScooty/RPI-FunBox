import requests, json
import serial
import adafruit_thermal_printer
import datetime
from healthCheck import *

def statusPrint():
    uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
    printer = ThermalPrinter(uart)

    mchost = "192.168.1.31"
    mcusername = "aidan"
    mcservice_name = "MC-Emergency-Bot.service"

    trhost = "192.168.1.61"
    trusername = "aidan"
    trservice_name = "trunk-recorder"

    mcEmergency = get_service_status(mchost, mcusername, mcservice_name)
    trunkRecorder = get_service_status(trhost, trusername, trservice_name)

    printer.print("###############################")
    printer.JUSTIFY_CENTER
    printer.print("  _____ _        _       ")
    printer.print(" / ____| |      | |      ")
    printer.print("| (___ | |_ __ _| |_ ___ ")
    printer.print(" \___ \| __/ _` | __/ __|")
    printer.print(" ____) | || (_| | |_\__ \\")
    printer.print("|_____/ \__\__,_|\__|___/")
    printer.JUSTIFY_LEFT
    printer.print("###############################")

    printer.feed(2)

    printer.print(mcEmergency)
    printer.feed(1)
    printer.print(trunkRecorder)
    printer.print("###############################")
    printer.feed(2)