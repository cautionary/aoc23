import numpy as np

inputdata = open('d21i01.txt', 'r')
lines = inputdata.readlines()

height = len(lines)
width = len(lines[0].strip())

rocks = set()

for r in range(height):
    for c in range(width):
        if lines[r][c] == 'S':
            start = complex(r,c)
        elif lines[r][c] == '#':
            rocks.add(complex(r,c))

positions = {start}

allpos = set()

vals = []
for i in range(328):
    newpos = set()
    for pos in positions:
        for n in [pos + 1j, pos - 1j, pos + 1+0j, pos - 1+0j]:
            if n not in rocks and n.real < height and n.imag < width and n.real >= 0 and n.imag >= 0:
                newpos.add(n)
            if complex(n.real % height, n.imag % width) not in rocks:
                allpos.add(n)
                newpos.add(n)

    positions = newpos.copy()
    if i + 1 == 65:
        vals.append(len(positions))
    if i + 1 == 196:
        vals.append(len(positions))
    if i + 1 == 327:
        vals.append(len(positions))


x = np.array([0, 1, 2])
y = np.array(vals)

print(round(np.polyval(np.polyfit(x, y, 2), 202300)))
