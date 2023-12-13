import paramiko
import json
import pytz
from datetime import datetime

def convert_timestamp_since(timestamp):
    if timestamp:
        est = pytz.timezone('US/Eastern')
        utc_time = datetime.utcfromtimestamp(int(timestamp) / 1e6).replace(tzinfo=pytz.utc)
        est_time = utc_time.astimezone(est)
        
        return est_time.strftime("%Y-%m-%d %H:%M:%S EST")
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
        stdout = ssh.exec_command(command)

        # Parse the JSON output
        output = stdout.read().decode("utf-8")
        entries = [json.loads(entry) for entry in output.strip().split("\n") if entry.strip()]
        if entries:
            entry = entries[0]
            status = entry.get("MESSAGE")
            since = convert_timestamp_since(int(entry.get("__REALTIME_TIMESTAMP")))
            uptime = convert_timestamp_uptime(int(entry.get("__MONOTONIC_TIMESTAMP")))

            out = "Service: " + service_name + "\nStatus: " + status + "\nSince: " + since + "\nUptime: " + uptime

            # Print the results
            # print(f"Service: {service_name}")
            # print(f"Status: {status}")
            # print(f"Since: {since}")
            # print(f"Uptime: {uptime}")

            return out
        else:
            return "Error - Service Not Found"

    except Exception as e:
        return "Error - " + e
    finally:
        # Close the SSH connection
        if ssh:
            ssh.close()
