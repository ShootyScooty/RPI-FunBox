import paramiko
import json
from datetime import datetime

def convert_timestamp_since(timestamp):
    if timestamp:
        return datetime.utcfromtimestamp(int(timestamp) / 1e6).strftime("%Y-%m-%d %H:%M:%S UTC")
    return "N/A"

def convert_timestamp_uptime(timestamp):
    if timestamp:
        seconds = int(timestamp) / 1e6
        days, remainder = divmod(seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    return "N/A"

def get_service_status(host, username, service_name):
    try:
        # SSH connection setup
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username)

        # Run journalctl command to get service status
        command = f"journalctl -u {service_name} -n 1 --output=json"
        stdin, stdout, stderr = ssh.exec_command(command)

        # Parse the JSON output
        output = stdout.read().decode("utf-8")
        entries = [json.loads(entry) for entry in output.strip().split("\n") if entry.strip()]
        if entries:
            entry = entries[0]
            status = entry.get("MESSAGE")
            since = convert_timestamp_since(int(entry.get("__REALTIME_TIMESTAMP")))
            uptime = convert_timestamp_uptime(int(entry.get("__MONOTONIC_TIMESTAMP")))

            # Print the results
            print(f"Service: {service_name}")
            print(f"Status: {status}")
            print(f"Since: {since}")
            print(f"Uptime: {uptime}")
        else:
            print(f"No journal entry found for service {service_name}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection
        if ssh:
            ssh.close()

if __name__ == "__main__":
    host = "192.168.1.31"
    username = "aidan"
    service_name = "MC-Emergency-Bot.service"

    get_service_status(host, username, service_name)
