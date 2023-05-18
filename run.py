import upnpclient

print("discovering devices...")

devices = upnpclient.discover()

if (len(devices) == 0):
    print("no devices discovered")
    exit()

print("\n")
print("choose device:")

for idx, device in enumerate(devices):
    print(str(idx) + ": " + str(device))

chosen_index = input()
device = devices[int(chosen_index)]


def do_service_action_loop():
    print("\n")
    print("choose service:")

    for idx, service in enumerate(device.services):
        print(str(idx) + ": " + str(service.service_id))

    chosen_service = input()
    full_service_id = device.services[int(chosen_service)].service_id
    service_id = full_service_id.split("serviceId:")[1]

    print("\n")
    print("choose action:")

    for idx, action in enumerate(device[service_id].actions):
        print(str(idx) + ": " + str(action))

    chosen_action = input()
    action = device[service_id].actions[int(chosen_action)]
    action_name = action.name

    action_to_invoke = device[service_id][action_name]
    action_args = action_to_invoke.argsdef_in

    if action_args == None or len(action_args) == 0:
        print("\n")
        print("invoking " + str(action_to_invoke))
        result = action_to_invoke()
        print(result)
        exit()

    input_args = {}
    for arg in action_args:
        print("\n")
        print(str(arg[0]) + ": ")
        input_arg = input()
        input_args[str(arg[0])] = input_arg

    print("invoking action " + str(action_to_invoke))
    result = action_to_invoke(**input_args)
    print(result)
    do_service_action_loop()


do_service_action_loop()
