from healthCheck import *

trhost = "192.168.1.61"
trusername = "aidan"
trservice_name = "trunk-recorder"

mchost = "192.168.1.31"
mcusername = "aidan"
mcservice_name = "MC-Emergency-Bot.service"

print(get_service_status(mchost, mcusername, mcservice_name))
print(get_service_status(trhost, trusername, trservice_name))
