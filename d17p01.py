from heapq import heappop, heappush

inputfile = open('d17i01.txt', 'r')
lines = inputfile.readlines()

height = len(lines)
width = len(lines[0].strip())

def get_neighbors(pos, direc, numstraight):
    coords = [pos + direc * turn for turn in [-1j, 1j]]
    if numstraight < 2:
        coords.append(pos + direc)

    return [coord for coord in coords if coord.real >= 0 and coord. imag >= 0 and coord.real < height and coord.imag < width]

distances = {}

for r in range(height):
    for c in range(width):
        for d in [1j, -1j, 1+0j, -1+0j]:
            for n in range(3):
                distances[(complex(r, c), d, n)] = 9223372036854775807


sptset = set()
numstraight = 0
direc = 1j

curnode = (0, 0)

distances[(0j, 1j, 0)] = 0

queue = [((0,0), (0,1), 0)]

while queue:
    (curnode, direc, numstraight) = heappop(queue)
    curnode = complex(curnode[0], curnode[1])
    direc = complex(direc[0], direc[1])
    sptset.add((curnode, direc, numstraight))
    ns = get_neighbors(curnode, direc, numstraight)

    for n in ns:
        weight = int(lines[int(n.real)][int(n.imag)])
        newdirec = n - curnode
        if direc == newdirec:
            newnumstraight = numstraight + 1
        else:
            newnumstraight = 0
        newdist = distances[(curnode, direc, numstraight)] + weight
        if newdist < distances[(n, newdirec, newnumstraight)]:
            distances[(n, newdirec, newnumstraight)] = newdist
            heappush(queue, ((int(n.real), int(n.imag)), (int(newdirec.real), int(newdirec.imag)), newnumstraight))


sps = []
for d in [1j, -1j, 1+0j, -1+0j]:
    for n in range(3):
        sps.append(distances[complex(height-1, width-1), d, n])

print(min(sps))

