import RPi.GPIO as GPIO
from weatherForecast import *
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
    print("Running Weather")
    weatherPrint()

def pushGreen(green):
    print("Green Pressed")

def pushYellow(yellow):
    print("Yellow Pressed")

def pushRed(red):
    print("Red Pressed")

def pushWhite(white):
    print("White Pressed")

GPIO.add_event_detect(blue, GPIO.RISING, callback=pushBlue, bouncetime=800)
GPIO.add_event_detect(green, GPIO.RISING, callback=pushGreen, bouncetime=800)
GPIO.add_event_detect(yellow, GPIO.RISING, callback=pushYellow, bouncetime=800)
GPIO.add_event_detect(red, GPIO.RISING, callback=pushRed, bouncetime=800)
GPIO.add_event_detect(white, GPIO.RISING, callback=pushWhite, bouncetime=800)

message = input("Press Enter to Quit\n\n")

print("Cleaning Up and Quitting")

GPIO.cleanup()