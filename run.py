import upnpclient

print("discovering devices...")

devices = upnpclient.discover()

if (len(devices) == 0):
    print("no devices discovered")
    exit()

print("choose device:")

for idx, device in enumerate(devices):
    print(str(idx) + ": " + str(device))

chosen_index = input()
device = devices[int(chosen_index)]

print("choose service:")

for idx, service in enumerate(device.services):
    print(str(idx) + ": " + str(service.service_id))

chosen_service = input()
full_service_id = device.services[int(chosen_service)].service_id
service_id = full_service_id.split("serviceId:")[1]

print("choose action:")

for idx, action in enumerate(device[service_id].actions):
    print(str(idx) + ": " + str(action))

chosen_action = input()
action = device[service_id].actions[int(chosen_action)]
action_name = action.name

print(device[service_id][action_name]())
