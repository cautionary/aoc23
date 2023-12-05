infile = open('d05i01.txt', 'r')

sections = infile.read().strip().split("\n\n")

seeds = []
for seed in sections[0].split(":")[1].split():
    seeds.append(int(seed))

maptypes = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
maps = {}
for i, section in enumerate(sections[1:]):
    maps[maptypes[i]] = []
    for line in section.split('\n')[1:]:
        maps[maptypes[i]].append(tuple(int(el) for el in line.split()))

location = 9223372036854775807
for seed in seeds:
    for maptype in maptypes:
        foundmap = False
        for ran in maps[maptype]:
            if not foundmap:
                if seed >= ran[1] and seed <= ran[1] + ran[2]:
                    seed += (ran[0] - ran[1])
                    foundmap = True

    location = min(location, seed)

print(location)
