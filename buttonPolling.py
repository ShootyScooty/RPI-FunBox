#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv/  
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
import RPi.GPIO as GPIO
from weatherForecast import *
GPIO.setmode(GPIO.BCM)

# Pin 23: Blue Button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

try:  
    GPIO.wait_for_edge(23, GPIO.FALLING)  
    weatherPrint()

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  