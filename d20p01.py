inputdata = open('d20i01.txt', 'r')
lines = inputdata.readlines()

modules = {}

for line in lines:
    src, dst = line.strip().split(' -> ')
    if src == "broadcaster":
        modules["broadcaster"] = {"type": "broadcaster", "dest": [x for x in dst.split(', ')]}
    elif src[0] == '%':
        modules[src[1:]] = {"type": src[0], "dest": [x for x in dst.split(', ')], "state": False}
    elif src[0] == '&':
        modules[src[1:]] = {"type": src[0], "dest": [x for x in dst.split(', ')], "states": {}}

for mod in modules:
    for dest in modules[mod]["dest"]:
        if dest in modules and modules[dest]["type"] == '&':
            modules[dest]["states"][mod] = 0


(lows, highs) = (0, 0)
for i in range(1000):
    queue = []
    queue.append(("broadcaster", 0, "button"))

    while queue:
        (mod, pulse, src) = queue.pop(0)
        if pulse:
            highs += 1
        else:
            lows+= 1
        if mod not in modules:
            pass
        elif modules[mod]["type"] == "broadcaster":
            for dest in modules[mod]["dest"]:
                queue.append((dest, pulse, mod))
        elif modules[mod]["type"] == '%':
            if pulse == 0:
                if modules[mod]["state"]:
                    modules[mod]["state"] = False
                    for dest in modules[mod]["dest"]:
                        queue.append((dest, 0, mod))
                else:
                    modules[mod]["state"] = True
                    for dest in modules[mod]["dest"]:
                        queue.append((dest, 1, mod))
        elif modules[mod]["type"] == '&':
            modules[mod]["states"][src] = pulse
            state = True
            for s in modules[mod]["states"]:
                if not modules[mod]["states"][s]:
                    state = False
            pulse = 0 if state else 1
            for dest in modules[mod]["dest"]:
                queue.append((dest, pulse, mod))


print(lows * highs)
