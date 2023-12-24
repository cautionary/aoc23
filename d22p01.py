inputdata = open('d22i01.txt', 'r')
lines = inputdata.readlines()

bricks = []
for line in lines:
    e1, e2 = line.strip().split('~')
    c1 = tuple([int(x) for x in e1.split(',')])
    c2 = tuple([int(x) for x in e2.split(',')])
    
    bricks.append((c1, c2))

bricks.sort(key=lambda x: x[1][2])
settled = []
cubes = {}

while(bricks):
    brick = bricks.pop(0)
    (x1, y1, z1), (x2, y2, z2) = brick
    issettled = False
    while not issettled:
        if z1 == 1:
            issettled = True
        else:
            canmove = True
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y, z1 - 1) in cubes:
                        canmove = False
            if canmove:
                z1 -= 1
                z2 -= 1
            else:
                issettled = True
            
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                cubes[(x, y, z)] = ((x1, y1, z1), (x2, y2, z2))
    settled.append(((x1, y1, z1), (x2, y2, z2)))
  

total = 0    
for brick in settled:
    (x1, y1, z1), (x2, y2, z2) = brick
    supported = set()
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if (x, y, z2 + 1) in cubes:
                supported.add(cubes[(x, y, z2 + 1)])

    safe = True
    
    if supported:
        for b2 in supported:
            (x1, y1, z1), (x2, y2, z2) = b2
            supports = set()
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y, z1 - 1) in cubes:
                        supports.add(cubes[(x, y, z1 - 1)])
            if len(supports) == 1:
                 safe = False
    if safe:
        total += 1


print(total)
