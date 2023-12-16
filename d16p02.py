inputfile = open('d16i01.txt')
lines = inputfile.readlines()

grid = [line.strip() for line in lines]


def ingrid(coord):
    if coord.real < len(grid)  and coord.real >= 0 and coord.imag < len(grid[0]) and coord.imag >= 0:
        return True

dirswap = {'\\': {1j: 1+0j, 1+0j: 1j, -1j: -1+0j, -1+0j: -1j},
            '/': {1j: -1+0j, -1+0j: 1j, -1j: 1+0j, 1+0j: -1j}}

best = 0

starts = []
for i in range(len(grid[0])):
    starts.append((complex(0, i), 1+0j))
    starts.append((complex(len(grid)-1, i), -1+0j))
for i in range(len(grid)):
    starts.append((complex(i, 0), 1j))
    starts.append((complex(i, len(grid)-1), -1j))


for start in starts:
    beams =[start]
    beamhist = set()
    visited = set()
    while beams:
        newbeams = []
        for bloc, bdir in beams:
            beamhist.add((bloc, bdir))
            visited.add(bloc)
            tile = grid[int(bloc.real)][int(bloc.imag)]

            if tile == '.' or tile == '-' and bdir.real == 0 or tile == '|' and bdir.imag == 0:
                if ingrid(bloc + bdir) and (bloc + bdir, bdir) not in beamhist:
                    newbeams.append((bloc + bdir, bdir))
            elif tile in ['\\', '/']:
                bdir = dirswap[tile][bdir]
                if ingrid(bloc + bdir) and (bloc + bdir, bdir) not in beamhist:
                    newbeams.append((bloc + bdir, bdir))
            elif tile == '-':
                b2dir = 1j
                b2loc = bloc + b2dir
                if ingrid(b2loc) and (b2loc, b2dir) not in beamhist:
                    beams.append((b2loc, b2dir))
                bdir = -1j
                if ingrid(bloc + bdir) and (bloc + bdir, bdir) not in beamhist:
                    newbeams.append((bloc + bdir, bdir))
            elif tile == '|':
                b2dir = 1+0j
                b2loc = bloc + b2dir
                if ingrid(b2loc) and (b2loc, b2dir) not in beamhist:
                    beams.append((b2loc, b2dir))
                bdir = -1+0j
                if ingrid(bloc + bdir) and (bloc + bdir, bdir) not in beamhist:
                    newbeams.append((bloc + bdir, bdir))

        beams = newbeams.copy()

    best = max(best, len(visited))

print(best)
