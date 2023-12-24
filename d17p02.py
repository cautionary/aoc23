from heapq import heappop, heappush

inputfile = open('d17i01.txt', 'r')
lines = inputfile.readlines()

height = len(lines)
width = len(lines[0].strip())

distances = {}

for r in range(height):
    for c in range(width):
        for d in [1j, -1j, 1+0j, -1+0j]:
            distances[(complex(r, c), d)] = 9223372036854775807

sptset = set()
numstraight = 0
direc = 1j

curnode = (0, 0)

distances[(0j, 1j)] = 0
distances[(0j, 1+0j)] = 0

queue = [((0,0), (0,1)), ((0,0), (1,0))]

while queue:
    (curnode, direc) = heappop(queue)
    curnode = complex(curnode[0], curnode[1])
    direc = complex(direc[0], direc[1])
    sptset.add((curnode, direc))
    
    posweight = 0
    negweight = 0
    for i in range(1, 11):
        if direc in [1j, -1j]:
            coord = curnode + complex(i,0)
            if coord.real >= 0 and coord.real < height and coord.imag >= 0 and coord.imag < width:
                posweight += int(lines[int(coord.real)][int(coord.imag)])
                if i >=4:
                    newdist = distances[(curnode, direc)] + posweight
                    if newdist < distances[(coord, 1+0j)]:
                        distances[(coord, 1+0j)] = newdist
                        heappush(queue, ((int(coord.real), int(coord.imag)), (1, 0))) 
            coord = curnode - complex(i,0)
            if coord.real >= 0 and coord.real < height and coord.imag >= 0 and coord.imag < width:
                negweight += int(lines[int(coord.real)][int(coord.imag)])
                if i >=4:
                    newdist = distances[(curnode, direc)] + negweight
                    if newdist < distances[(coord, (-1+0j))]:
                        distances[(coord, -1+0j)] = newdist
                        heappush(queue, ((int(coord.real), int(coord.imag)), (-1, 0))) 
        else:
            coord = curnode + complex(0,i)
            if coord.real >= 0 and coord.real < height and coord.imag >= 0 and coord.imag < width:
                posweight += int(lines[int(coord.real)][int(coord.imag)])
                if i >=4:
                    newdist = distances[(curnode, direc)] + posweight
                    if newdist < distances[(coord, 1j)]:
                        distances[(coord, 1j)] = newdist
                        heappush(queue, ((int(coord.real), int(coord.imag)), (0, 1))) 
            coord = curnode - complex(0,i)
            if coord.real >= 0 and coord.real < height and coord.imag >= 0 and coord.imag < width:
                negweight += int(lines[int(coord.real)][int(coord.imag)])
                if i >=4:
                    newdist = distances[(curnode, direc)] + negweight
                    if newdist < distances[(coord, -1j)]:
                        distances[(coord, -1j)] = newdist
                        heappush(queue, ((int(coord.real), int(coord.imag)), (0, -1))) 



sps = []
for d in [1j, -1j, 1+0j, -1+0j]:
    sps.append(distances[complex(height-1, width-1), d])

print(min(sps))

#1001 too high
