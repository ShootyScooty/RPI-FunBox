import paramiko
from cysystemd import journal

def get_service_status(host, username, service_name):
    try:
        # SSH connection setup
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username)

        # Get service status using cysystemd
        with journal.Reader() as reader:
            reader.add_match(_SYSTEMD_UNIT=service_name)
            reader.seek_tail()

            # Retrieve the last entry for the specified service
            entry = reader.get_previous()
            
            if entry:
                status = entry.get('MESSAGE')
                since = entry.get('__REALTIME_TIMESTAMP')
                uptime = entry.get('__MONOTONIC_TIMESTAMP')

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
