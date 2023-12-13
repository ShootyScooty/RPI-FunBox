import RPi.GPIO as GPIO
from weatherForecast import *
from emergencyFeed import *
from healthCheck import *
from newsFeed import *
from printerTest import *
GPIO.setwarnings(False)

# GPIO Broadcom Pin Assignment Number
# GPIO.setmode(GPIO.BCM)
# blue = 23
# green = 24
# yellow = 25
# red = 12
# white = 16

# PI Physical Pin Number
GPIO.setmode(GPIO.BOARD)
blue = 16
green = 18
yellow = 22
red = 32
white = 36

GPIO.setup(blue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(yellow, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(white, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def pushBlue(blue):
    if GPIO.input(blue) == GPIO.HIGH:
        print("Running Weather")
        weatherPrint()

def pushGreen(green):
    if GPIO.input(green) == GPIO.HIGH:
        print("Running Stats")
        healthPrint()

def pushYellow(yellow):
    if GPIO.input(yellow) == GPIO.HIGH:
        print("Running News")
        printNews()

def pushRed(red):
    if GPIO.input(red) == GPIO.HIGH:
        print("Running Emergency")
        printEmergency()

def pushWhite(white):
    if GPIO.input(white) == GPIO.HIGH:
        print("White Pressed")
        printTest()

GPIO.add_event_detect(blue, GPIO.RISING, callback=pushBlue, bouncetime=200)
GPIO.add_event_detect(green, GPIO.RISING, callback=pushGreen, bouncetime=200)
GPIO.add_event_detect(yellow, GPIO.RISING, callback=pushYellow, bouncetime=200)
GPIO.add_event_detect(red, GPIO.RISING, callback=pushRed, bouncetime=200)
GPIO.add_event_detect(white, GPIO.RISING, callback=pushWhite, bouncetime=200)

message = input("Press Enter to Quit\n\n")

print("Cleaning Up and Quitting")

GPIO.cleanup()