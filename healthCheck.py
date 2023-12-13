import subprocess

print(subprocess.check_output(['systemctl', '--host', 'aidan@192.168.1.31', 'status', 'MC-Emergency-Bot']))