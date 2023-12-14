import re
infile = open('d12i01.txt', 'r')
lines = infile.readlines()

total = 0
for line in lines:
    record = line.strip().split()
    pattern = "(^|^\.+)"
    counts = record[1].split(',')
    for i, count in enumerate(counts):
        for j in range(int(count)):
            pattern += "#"
        if i != len(counts) - 1:
            pattern += "\.+"
    pattern += "($|\.+$)"

    unknowns = [i for i, char in enumerate(record[0]) if char == '?']
    for i in range(2 ** len(unknowns)):
        bytemap = bin(i)[2:].zfill(len(unknowns))

        unkmap = bytemap.replace('0', '.').replace('1', '#')
        row = ""
        unkcount = 0
        for i, char in enumerate(record[0]):
            if char == '?':
                row += unkmap[unkcount]
                unkcount += 1
            else:
                row += char

        if re.match(pattern, row):
            total += 1

print(total)

