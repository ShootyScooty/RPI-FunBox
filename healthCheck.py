import paramiko
import systemd

def get_service_status(host, username, service_name):
    try:
        # SSH connection setup
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username)

        # Get service status using systemd
        manager = systemd.manager.Manager()
        service = manager.get_unit(service_name)
        status = service.properties["ActiveState"]
        since = service.properties["ActiveEnterTimestampMonotonic"]
        uptime = service.properties["ActiveEnterTimestampMonotonic"]

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

# import subprocess

# out = str(subprocess.check_output(['cat', 'botHealth.py', '|', 'ssh', 'aidan@192.168.1.31', 'python', '-']))

# print(out)

# mcBot = out.split("\n     ")

# for x in mcBot:
#     print(x)