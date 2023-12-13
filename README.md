# RPI-FunBox

## References
https://github.com/adafruit/Python-Thermal-Printer
https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython
https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

## API Sources
https://openweathermap.org/current
https://openweathermap.org/forecast5
https://www.monroecounty.gov/incidents911.rss
https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1077
https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1654

## For Raspberry Pi

### Hardware Setup
* `sudo raspi-config`
* > Interface Options
* > Login Shell: NO
* > Serial Port Hardware: YES
* Reboot

![printer-to-pi](https://github.com/aidan-lemay/RPI-FunBox/assets/34166033/3c49a892-93da-4817-ac5a-a91879448cd5)
![printer-to-header](https://github.com/aidan-lemay/RPI-FunBox/assets/34166033/d9d9eac8-ef65-47c9-9c2b-59289bc0cee5)
![gpio](https://github.com/aidan-lemay/RPI-FunBox/assets/34166033/0cbffadd-883f-4266-a181-dd581589301d)

### Software Setup
`sudo pip3 install adafruit-circuitpython-thermal-printer`
- OR -
`python3 -m venv .venv`
`source .venv/bin/activate`
`python3 -m pip install adafruit-circuitpython-thermal-printer`

For all future instructions, prepend `install` with either `sudo pip3` or `python3 -m pip` depending on your above choosings

`install requests`
`install requests_html`
`install paramiko`
`install cysystemd`

Get an API key from here - https://openweathermap.org/appid

Create key.py in the root project directory with the following: `API_KEY = "<Your API Key from openweathermap>"`
