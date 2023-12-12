infile = open('d10i01.txt', 'r')
lines = infile.readlines()


groundtiles = set()
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if lines[i][j] == 'S':
            start = complex(i, j)
        elif lines[i][j] == '.':
            groundtiles.add(complex(i, j))


looptiles = set()
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
    looptiles.add(pos)
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

outsidetiles = set()

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if complex(i, j) not in looptiles:
            groundtiles.add(complex(i, j))


for groundtile in groundtiles.copy():
    testline = ""
    for i in range(int(groundtile.imag)):
        if complex(groundtile.real, i) in looptiles:
            testline = testline + lines[int(groundtile.real)][i]

    tiles = testline.replace('-', '').replace('FJ', '|').replace('F7', '').replace('LJ', '').replace('L7', '|').replace('S', '|')

    if tiles.count('|') % 2 == 0:
        groundtiles.remove(groundtile)
        

#for i, line in enumerate(lines):
#    if i < 100:
#        print(' ', end='')
#    if i < 10:
#        print(' ', end='')
#    print("%d " % i, end='')
#    for j, c in enumerate(line):
#        if complex(i, j) in looptiles:
#            print(c, end = '')
#        elif complex(i, j) in groundtiles:
#            print('▩', end='')
#        elif complex(i, j) in outsidetiles:
#            print('0', end='')
#        else:
#            print(' ', end='')
#    print()



print(len(groundtiles))
