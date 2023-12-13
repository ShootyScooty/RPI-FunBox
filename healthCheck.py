import subprocess

out = subprocess.check_output(['systemctl', '--host', 'aidan@192.168.1.31', 'status', 'MC-Emergency-Bot'])

mcBot = out.split("\n     ")

for x in mcBot:
    print(x)


# b'\xe2\x97\x8f MC-Emergency-Bot.service - MC Emergency Bot\n     Loaded: loaded (/etc/systemd/system/MC-Emergency-Bot.service; enabled; preset: enabled)\n     Active: active (running) since Mon 2023-12-11 11:41:08 EST; 1 day 23h ago\n   Main PID: 1031\n      Tasks: 2 (limit: 9342)\n     Memory: 56.2M\n        CPU: 7.697s\n     CGroup: /system.slice/MC-Emergency-Bot.service\n             \xe2\x94\x94\xe2\x94\x801031 /home/aidan/venv/mc-emergency/bin/python3 /home/aidan/Git-Projects/MC-Emergency-Bot/bot.py\n'