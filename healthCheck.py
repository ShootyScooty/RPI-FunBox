import paramiko
from cysystemd import journal

def get_service_status(host, username, service_name):
    try:
        # SSH connection setup
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username)

        # Get service status using cysystemd.journal
        with journal.Reader() as reader:
            reader.seek_unit(service_name)
            event = reader.get_next()
            status = event['MESSAGE']
            since = event['__REALTIME_TIMESTAMP']
            uptime = event['__MONOTONIC_TIMESTAMP']

        # Print the results
        print(f"Service: {service_name}")
        print(f"Status: {status}")
        print(f"Since: {since}")
        print(f"Uptime: {uptime}")

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
