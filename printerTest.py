from healthCheck import *

trhost = "192.168.1.61"
trusername = "aidan"
trservice_name = "trunk-recorder"

print(get_service_status(trhost, trusername, trservice_name))