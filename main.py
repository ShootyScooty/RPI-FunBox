import Adafruit_Thermal

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)



# Leave at end
printer.feed(2)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults