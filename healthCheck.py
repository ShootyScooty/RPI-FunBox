import paramiko
import json
import pytz
import requests, json
import serial
import adafruit_thermal_printer
import datetime
import urllib.request
from datetime import datetime
from printerTools import *

def convert_timestamp_since(timestamp):
    if timestamp:
        est = pytz.timezone('US/Eastern')
        utc_time = datetime.utcfromtimestamp(int(timestamp) / 1e6).replace(tzinfo=pytz.utc)
        est_time = utc_time.astimezone(est)
        
        return est_time.strftime("%Y-%m-%d %H:%M:%S EST")
    return "N/A"

def convert_timestamp_uptime(timestamp):
    if timestamp:
        seconds = int(timestamp) / 1e6
        days, remainder = divmod(seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    return "N/A"

def get_service_status(host, username, service_name):
    try:
        # SSH connection setup
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username)

        # Run journalctl command to get service status
        command = f"journalctl -u {service_name} -n 1 --output=json"
        stdin, stdout, stderr = ssh.exec_command(command)

        # Parse the JSON output
        output = stdout.read().decode("utf-8")
        entries = [json.loads(entry) for entry in output.strip().split("\n") if entry.strip()]
        if entries:
            entry = entries[0]
            status = entry.get("MESSAGE")
            since = convert_timestamp_since(int(entry.get("__REALTIME_TIMESTAMP")))
            uptime = convert_timestamp_uptime(int(entry.get("__MONOTONIC_TIMESTAMP")))

            # out = "Service: " + service_name + "\nStatus: " + status + "\nSince: " + since + "\nUptime: " + uptime
            out = "Service: " + service_name + "\nSince: " + since + "\nUptime: " + uptime

            # Print the results
            # print(f"Service: {service_name}")
            # print(f"Status: {status}")
            # print(f"Since: {since}")
            # print(f"Uptime: {uptime}")

            return out
        else:
            return "Error - Service Not Found"

    except Exception as e:
        return "Error - " + str(e)
    finally:
        # Close the SSH connection
        if ssh:
            ssh.close()

def healthPrint():
    uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
    printer = ThermalPrinter(uart)

    mchost = "192.168.1.31"
    mcusername = "aidan"
    mcservice_name = "MC-Emergency-Bot.service"

    trhost = "192.168.1.61"
    trusername = "aidan"
    trservice_name = "trunk-recorder.service"

    mcEmergency = get_service_status(mchost, mcusername, mcservice_name)
    trunkRecorder = get_service_status(trhost, trusername, trservice_name)

    com = ""
    tech = ""

    try:
        com = "https://aidanlemay.com/ responded with a code of " + str(urllib.request.urlopen("https://aidanlemay.com/").getcode())
    except Exception:
        com = "Unable to reach https://aidanlemay.com/"

    try:
        tech = "https://k5doc.tech/ responded with a code of " + str(urllib.request.urlopen("https://k5doc.tech/").getcode())
    except Exception:
        tech = "Unable to reach https://k5doc.tech/"

    printer.print("###############################")
    printer.print(center_text("  _____ _        _       "))
    printer.print(center_text(" / ____| |      | |      "))
    printer.print(center_text("| (___ | |_ __ _| |_ ___ "))
    printer.print(center_text(" \___ \| __/ _` | __/ __|"))
    printer.print(center_text(" ____) | || (_| | |_\__ \\"))
    printer.print(center_text("|_____/ \__\__,_|\__|___/"))
    printer.print("###############################")

    printer.feed(2)

    printer.print(mcEmergency)
    printer.feed(1)
    printer.print(trunkRecorder)
    printer.feed(1)
    printer.print("###############################")
    printer.feed(1)
    printer.print(com)
    printer.feed(1)
    printer.print(tech)
    printer.feed(1)
    printer.print("###############################")
    printer.feed(2)