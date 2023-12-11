infile = open('d10s03.txt', 'r')
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

for groundtile in groundtiles.copy():
    crossedtiles = set()
    if groundtile.real < len(lines) / 3:
        remove = True
        for i in range(int(groundtile.real), -1, -1):
            crossedtiles.add(complex(i, groundtile.imag))
            if complex(i, groundtile.imag) in looptiles:
                remove = False
        if remove:
            groundtiles.remove(groundtile)
            outsidetiles.update(crossedtiles)
    crossedtiles.clear()
    if groundtile.real > len(lines) - len(lines) / 3:
        if groundtile in groundtiles:
            remove = True
            for i in range(int(groundtile.real), len(lines)):
                crossedtiles.add(complex(i, groundtile.imag))
                if complex(i, groundtile.imag) in looptiles:
                    remove = False
            if remove:
                groundtiles.remove(groundtile)
                outsidetiles.update(crossedtiles)
    crossedtiles.clear()
    if groundtile.imag < len(lines[0]) / 3:
        if groundtile in groundtiles:
            remove = True
            for i in range(int(groundtile.imag), -1, -1):
                crossedtiles.add(complex(groundtile.real, i))
                if complex(groundtile.real, i) in looptiles:
                    remove = False
            if remove:
                outsidetiles.update(crossedtiles)
                groundtiles.remove(groundtile)
    if groundtile.imag > len(lines[0]) - len(lines[0]) / 3:
        if groundtile in groundtiles:
            remove = True
            for i in range(int(groundtile.imag), len(lines[0])):
                crossedtiles.add(complex(groundtile.real, i))
                if complex(groundtile.real, i) in looptiles:
                    remove = False
            if remove:
                outsidetiles.update(crossedtiles)
                groundtiles.remove(groundtile)
            
for groundtile in groundtiles.copy():
    allchecked = False
    visited = set()
    possible = {groundtile}
    while not allchecked:
        curpos = possible.pop()
        visited.add(curpos)
        if curpos in outsidetiles:
            groundtiles.remove(groundtile)
            allchecked = True
        if curpos.real.is_integer() and curpos.imag.is_integer():
            for i, nextpos in enumerate([curpos-1, curpos+1, curpos-1j, curpos+1j]):
                if nextpos not in visited:
                    if nextpos in looptiles:
                        tile = lines[int(nextpos.real)][int(nextpos.imag)]
                        if i in [0,1]:
                            if tile == '-':
                                visited.add(nextpos)
                            elif tile in ['|', 'J', '7']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag+1)] in ['|', 'F', 'L']:
                                    if nextpos + 0.5j not in possible and nextpos + 0.5j not in visited:
                                        possible.add(nextpos + 0.5j)
                            elif tile in ['|', 'F', 'L']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag-1)] in ['|', 'J', '7']:
                                    if nextpos - 0.5j not in possible and nextpos - 0.5j not in visited:
                                        possible.add(nextpos - 0.5j)
                        elif i in [2,3]:
                            if tile == '|':
                                visited.add(nextpos)
                            elif tile in ['-', 'J', 'L']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real+1)][int(nextpos.imag)] in ['-', '7', 'F']:
                                    if nextpos + 0.5 not in possible and nextpos + 0.5 not in visited:
                                        possible.add(nextpos + 0.5)
                            elif tile in ['-', '7', 'F']:
                                if lines[int(nextpos.real-1)][int(nextpos.imag)] in ['-', 'J', 'L']:
                                    if nextpos - 0.5 not in possible and nextpos - 0.5 not in visited:
                                        possible.add(nextpos - 0.5)
                    else:
                        possible.add(nextpos)

        elif not curpos.imag.is_integer():
            for i, nextpos in enumerate([curpos - 1 - 0.5j, curpos - 1 + 0.5j, curpos + 1 - 0.5j, curpos +1 + 0.5j]):
                if nextpos not in visited:
                    if nextpos in looptiles:
                        tile = lines[int(nextpos.real)][int(nextpos.imag)]
                        if i == 0:
                            if tile == '-':
                                visited.add(nextpos)
                            elif tile in ['|', 'J', '7']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag+1)] in ['|', 'F', 'L']:
                                    if nextpos + 0.5j not in possible and nextpos + 0.5j not in visited:
                                        possible.add(nextpos + 0.5j)
                            elif tile in ['|', 'F', 'L']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag-1)] in ['|', 'J', '7']:
                                    if nextpos - 0.5j not in possible and nextpos - 0.5j not in visited:
                                        possible.add(nextpos - 0.5j)
                        elif i == 2:
                            if tile == '-':
                                visited.add(nextpos)
                            elif tile in ['|', 'J', '7']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag+1)] in ['|', 'F', 'L']:
                                    if nextpos + 0.5j not in possible and nextpos + 0.5j not in visited:
                                        possible.add(nextpos + 0.5j)
                            elif tile in ['|', 'F', 'L']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag-1)] in ['|', 'J', '7']:
                                    if nextpos - 0.5j not in possible and nextpos - 0.5j not in visited:
                                        possible.add(nextpos - 0.5j)

                    else:
                        possible.add(nextpos)

        elif not curpos.real.is_integer():
            for i, nextpos in enumerate([curpos - 0.5 - 1j, curpos - 0.5 + 1j, curpos + 0.5 - 1j, curpos + 0.5 + 1j]):
                if nextpos not in visited:
                    if nextpos in looptiles:
                        tile = lines[int(nextpos.real)][int(nextpos.imag)]
                        if i == 0:
                            if tile == '|':
                                visited.add(nextpos)
                            elif tile in ['-', 'J', 'L']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag+1)] in ['-', 'F', '7']:
                                    if nextpos + 0.5 not in possible and nextpos + 0.5 not in visited:
                                        possible.add(nextpos + 0.5)
                            elif tile in ['-', 'F', '7']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag-1)] in ['-', 'J', 'L']:
                                    if nextpos - 0.5 not in possible and nextpos - 0.5 not in visited:
                                        possible.add(nextpos - 0.5)
                        elif i == 2:
                            if tile == '|':
                                visited.add(nextpos)
                            elif tile in ['-', 'J', 'L']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag+1)] in ['-', 'F', '7']:
                                    if nextpos + 0.5 not in possible and nextpos + 0.5 not in visited:
                                        possible.add(nextpos + 0.5)
                            elif tile in ['-', 'F', '7']:
                                visited.add(nextpos)
                                if lines[int(nextpos.real)][int(nextpos.imag-1)] in ['-', 'J', 'L']:
                                    if nextpos - 0.5 not in possible and nextpos - 0.5 not in visited:
                                        possible.add(nextpos - 0.5)
                    else:
                        possible.add(nextpos)

                
        print(curpos, possible, visited)
                
        if not possible:
            allchecked = True
    print()

for i, line in enumerate(lines):
    if i < 100:
        print(' ', end='')
    if i < 10:
        print(' ', end='')
    print("%d " % i, end='')
    for j, c in enumerate(line):
        if complex(i, j) in looptiles:
            print(c, end = '')
        elif complex(i, j) in groundtiles:
            print('▩', end='')
        elif complex(i, j) in outsidetiles:
            print('0', end='')
        else:
            print(' ', end='')
    print()

#46


print(len(groundtiles))
