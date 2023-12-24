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
supporting = {}
supportedby = {}

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
    supporting[brick] = set()
    (x1, y1, z1), (x2, y2, z2) = brick
    supported = set()
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if (x, y, z2 + 1) in cubes:
                supported.add(cubes[(x, y, z2 + 1)])

    for b2 in supported:
        supporting[brick].add(b2)
        if not b2 in supportedby:
            supportedby[b2] = {brick}
        else:
            supportedby[b2].add(brick)


for brick in settled:
    affected = {brick}
    checks = [brick]
    while checks:
        b1 = checks.pop(0)
        for b2 in supporting[b1]:
            if supportedby[b2].issubset(affected):
                affected.add(b2)
                checks.append(b2)

    total += len(affected) - 1




print(total)
