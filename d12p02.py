import re
infile = open('d12s01.txt', 'r')
lines = infile.readlines()

total = 0
for line in lines:
    record = line.strip().split()
    cond = record[0]
    for _ in range(4):
        cond += "?" + record[0]
    pattern = "(^|^[\.?]+)"
    counts = []
    for _ in range(5):
        counts += record[1].split(',')
    for i, count in enumerate(counts):
        for j in range(int(count)):
            pattern += "[#?]"
        if i != len(counts) - 1:
            pattern += "[\.?]+"
    pattern += "($|[\.?]+$)"

    unknowns = [i for i, char in enumerate(cond) if char == '?']

    print(len(unknowns))
    for unk in unknowns.copy():
        dotrecord = cond[0:unk] + "." + cond[unk+1:]
        dotmatch = re.match(pattern, dotrecord)
        hashrecord = cond[0:unk] + "#" + cond[unk+1:]
        hashmatch = re.match(pattern, hashrecord)
        if dotmatch and not hashmatch:
            cond = dotrecord
            unknowns.remove(unk)
        elif hashmatch and not dotmatch:
            cond = hashrecord
            unknowns.remove(unk)
    print(len(unknowns))
    print()
#    for i in range(2 ** len(unknowns)):
#        bytemap = bin(i)[2:].zfill(len(unknowns))
#
#        unkmap = bytemap.replace('0', '.').replace('1', '#')
#        row = ""
#        unkcount = 0
#        for i, char in enumerate(record[0]):
#            if char == '?':
#                row += unkmap[unkcount]
#                unkcount += 1
#            else:
#                row += char
#
#        if re.match(pattern, row):
#            total += 1

print(total)

