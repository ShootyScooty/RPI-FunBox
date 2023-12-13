import subprocess

out = subprocess.check_output(['systemctl', '--host', 'aidan@192.168.1.31', 'status', 'MC-Emergency-Bot'])

mcBot = out.split()

for x in mcBot:
    print(x)