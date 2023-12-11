infile = open('d10i01.txt', 'r')
lines = infile.readlines()


for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if lines[i][j] == 'S':
            start = complex(i, j)

loopdone = False
count = 0
nextdir = 'S'
pos = start
while not loopdone:
    if nextdir == 'S':
        pos = pos + 1
    elif nextdir == 'N':
        pos = pos - 1
    elif nextdir == 'W':
        pos = pos - 1j
    elif nextdir == 'E':
        pos = pos + 1j

    tile = lines[int(pos.real)][int(pos.imag)]
    if tile == 'L':
        if nextdir == 'S':
            nextdir = 'E'
        elif nextdir == 'W':
            nextdir = 'N'
    elif tile == 'J':
        if nextdir == 'S':
            nextdir = 'W'
        elif nextdir == 'E':
            nextdir = 'N'
    elif tile == '7':
        if nextdir == 'N':
            nextdir = 'W'
        elif nextdir == 'E':
            nextdir = 'S'
    elif tile == 'F':
        if nextdir == 'N':
            nextdir = 'E'
        elif nextdir == 'W':
            nextdir = 'S'
    elif tile == 'S':
        loopdone = True
    count += 1
print(int(count/2))
