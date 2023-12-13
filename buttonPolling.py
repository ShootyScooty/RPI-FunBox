#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv/  
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
import RPi.GPIO as GPIO
from weatherForecast import *
GPIO.setmode(GPIO.BCM)

# Pin 23: Blue Button
blue = 23
green = 24
yellow = 25
red = 12
clear = 16

GPIO.setup(blue, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(yellow, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(red, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(clear, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Polling Started")

try:  
    while True:
        GPIO.wait_for_edge(blue, GPIO.FALLING)
        print("Running Weather")
        weatherPrint()

except KeyboardInterrupt:
    print("Shutting Down Polling")
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  