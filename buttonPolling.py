#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv/  
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
import RPi.GPIO as GPIO
from weatherForecast import *
GPIO.setmode(GPIO.BOARD)

# GPIO Pin Assignment Number
# blue = 23
# green = 24
# yellow = 25
# red = 12
# white = 16

# PI Actual Pin Number
blue = 16
green = 18
yellow = 22
red = 32
white = 36

GPIO.setup(blue, GPIO.IN)
GPIO.setup(green, GPIO.IN)
GPIO.setup(yellow, GPIO.IN)
GPIO.setup(red, GPIO.IN)
GPIO.setup(white, GPIO.IN)

GPIO.input(blue)
GPIO.input(green)
GPIO.input(yellow)
GPIO.input(red)
GPIO.input(white)

def pushBlue():
    print("Blue Pressed")

def pushGreen():
    print("Green Pressed")

def pushYellow():
    print("Yellow Pressed")

def pushRed():
    print("Red Pressed")

def pushWhite():
    print("White Pressed")

GPIO.add_event_detect(blue, GPIO.BOTH, callback=pushBlue, bouncetime=800)
GPIO.add_event_detect(green, GPIO.BOTH, callback=pushGreen, bouncetime=800)
GPIO.add_event_detect(yellow, GPIO.BOTH, callback=pushYellow, bouncetime=800)
GPIO.add_event_detect(red, GPIO.BOTH, callback=pushRed, bouncetime=800)
GPIO.add_event_detect(white, GPIO.BOTH, callback=pushWhite, bouncetime=800)

while True:
    print("Polling Started")

# try:  
#     while True:
#         GPIO.wait_for_edge(blue, GPIO.FALLING)
#         print("Running Weather")
#         weatherPrint()

# except KeyboardInterrupt:
#     print("Shutting Down Polling")
#     GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
# GPIO.cleanup()           # clean up GPIO on normal exit  