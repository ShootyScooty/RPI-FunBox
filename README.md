# RPI-FunBox

## References
https://github.com/adafruit/Python-Thermal-Printer

https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython

https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

https://patorjk.com/software/taag/#p=display&h=0&v=0&f=Big (Using font "Big", character width "Full" or "Smush(R)" depending on space)

## API Sources
https://openweathermap.org/current

https://openweathermap.org/forecast5

https://www.monroecounty.gov/incidents911.rss

https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1077

https://clearcutradio.app/api/v1/calls?system=us-ny-monroe&talkgroup=1654

https://newsapi.org/docs

https://api-ninjas.com

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
`python3 -m venv venv`

`source venv/bin/activate`

`python3 -m pip install adafruit-circuitpython-thermal-printer`

`python3 -m pip install requests`

`python3 -m pip install requests_html`

`python3 -m pip install paramiko`

`python3 -m pip install cysystemd`

`python3 -m pip install pytz`

Get an API key from here - https://openweathermap.org/appid

Get an API key from here - https://newsapi.org

Get an API key from here - https://api-ninjas.com

Create key.py in the root project directory with the following: 
```python
    WEATHER_API_KEY = "<Your API Key from openweathermap>"
    NEWS_API_KEY = "<Your API Key from newsapi>"
    NINJA_API_KEY = "<Your API Key from api-ninjas>"
```

#### SystemD Service Setup
Create the following in `/etc/systemd/system/buttons.service
```bash
[Unit]
Description=Button Box Listener
After=network.target
StartLimitIntervalSec=5

[Service]
Type=simple
Restart=always
RestartSec=1
User=buttonbox
ExecStart=/home/buttonbox/venv/bin/python3 /home/buttonbox/RPI-FunBox/buttonPolling.py
WorkingDirectory=/home/buttonbox/RPI-FunBox

[Install]
WantedBy=multi-user.target
```

Start with `sudo systemctl enable --now buttons`

See logs with `sudo journalctl -feu buttons`
