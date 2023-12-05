infile = open('d05i01.txt', 'r')

sections = infile.read().strip().split("\n\n")

seedranges = []
seedsection = sections[0].split(":")[1].split()
        
for i in range(0, len(seedsection), 2):
    seedranges.append((int(seedsection[i]), int(seedsection[i]) + int(seedsection[i+1]) - 1))


maptypes = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
maps = {}
for i, section in enumerate(sections[1:]):
    maps[maptypes[i]] = []
    for line in section.split('\n')[1:]:
        maps[maptypes[i]].append(tuple(int(el) for el in line.split()))

def split_range(seedrange, dest):
    split_ranges = []
    in_ranges = [seedrange]
    out_ranges = []
    while in_ranges:
        for in_range in in_ranges[:]:
            src_min = in_range[0]
            src_max = in_range[1]
            foundmatch = False
            for destrange in maps[dest]:
                tgt_min = destrange[1]
                tgt_max = destrange[1] + destrange[2] - 1
                if not foundmatch:
                    if src_min >= tgt_min and src_max <= tgt_max:
                        out_ranges.append(in_range)
                        in_ranges.remove(in_range)
                        foundmatch = True
                    elif src_min >= tgt_min and src_min <= tgt_max:
                        in_ranges.remove(in_range)
                        out_ranges.append((src_min, tgt_max))
                        in_ranges.append((tgt_max + 1, src_max))
                        foundmatch = True
                    elif src_max <= tgt_max and src_max >= tgt_min:
                        in_ranges.remove(in_range)
                        out_ranges.append((tgt_min, src_max))
                        in_ranges.append((src_min, tgt_min - 1))
                        foundmatch = True
            if not foundmatch:
                in_ranges.remove(in_range)
                out_ranges.append(in_range)
    return(out_ranges)

def map_range(seedrange, dest):
    src_min = seedrange[0]
    src_max = seedrange[1]
    for destrange in maps[dest]:
        tgt_min = destrange[1]
        tgt_max = destrange[1] + destrange[2] - 1
        if src_min >= tgt_min and src_max <= tgt_max:
            return((src_min + destrange[0] - destrange[1], src_max + destrange[0] - destrange[1]))
    return(seedrange)
    
for maptype in maptypes:
    newseedranges = []
    for seedrange in seedranges:
        newseedranges += split_range(seedrange, maptype)

    seedranges = newseedranges.copy()
    newseedranges = []

    for seedrange in seedranges:
        newseedranges.append(map_range(seedrange, maptype))

    seedranges = newseedranges.copy()


location = 9223372036854775807
for (seedrange, _) in newseedranges:
    location = min(location, seedrange)

print(location)
