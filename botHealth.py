import subprocess, re

def read_status(service):
    p =  subprocess.Popen(["systemctl", "status",  service], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    output = output.decode('utf-8')

    service_regx = r"Loaded:.*\/(.*service);"
    status_regx= r"Active:(.*) since (.*);(.*)"
    service_status = {}
    for line in output.splitlines():
        service_search = re.search(service_regx, line)
        status_search = re.search(status_regx, line)

        if service_search:
            service_status['service'] = service_search.group(1)
            #print("service:", service)

        elif status_search:
            service_status['status'] = status_search.group(1).strip()
            #print("status:", status.strip())
            service_status['since'] = status_search.group(2).strip()
            #print("since:", since.strip())
            service_status['uptime'] = status_search.group(3).strip()
            #print("uptime:", uptime.strip())

    return service_status

def main():
    service = 'MC-Emergency-Bot'
    reponse = read_status(service)

    for key in reponse:
        print('{}:{}'.format(key, reponse[key]))


if __name__ == '__main__':
    main()