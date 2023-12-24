inputdata = open('d24i01.txt', 'r')
lines = inputdata.readlines()

hailstones = []

def find_intersection(x1,y1,x2,y2,x3,y3,x4,y4):
        if (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) == 0 or (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ==0:
            return [0,0]
        px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
        py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        return [px, py]


for line in lines:
    (px, py, pz) = [int(x) for x in line.split(' @ ')[0].split(', ')]
    (vx, vy, vz) = [int(x) for x in line.split(' @ ')[1].split(', ')]
    hailstones.append(((px, py, pz), (vx, vy, vz)))


bounds = (200000000000000, 400000000000000)
pairs = set()
total = 0
for hs1 in hailstones:
    for hs2 in hailstones:
        if hs1 != hs2 and (hs1, hs2) not in pairs and (hs2, hs1) not in pairs:
            pairs.add((hs1, hs2))
            intersection = find_intersection(hs1[0][0],
                                              hs1[0][1],
                                              hs1[0][0] + hs1[1][0],
                                              hs1[0][1] + hs1[1][1],
                                              hs2[0][0],
                                              hs2[0][1],
                                              hs2[0][0] + hs2[1][0],
                                              hs2[0][1] + hs2[1][1])
            
            if (intersection[0] >= bounds[0] 
                and intersection[0] <= bounds[1] 
                and intersection[1] >= bounds[0]
                and intersection[1] <= bounds[1]):
                if ((hs1[1][0] > 0 and intersection[0] > hs1[0][0]
                    or hs1[1][0] < 0 and intersection[0] < hs1[0][0])
                    and (hs1[1][1] > 0 and intersection[1] > hs1[0][1] 
                    or hs1[1][1] < 0 and intersection[1] < hs1[0][1])
                    and (hs2[1][0] > 0 and intersection[0] > hs2[0][0]
                    or hs2[1][0] < 0 and intersection[0] < hs2[0][0])
                    and (hs2[1][1] > 0 and intersection[1] > hs2[0][1] 
                    or hs2[1][1] < 0 and intersection[1] < hs2[0][1])):

                    total += 1

print(total)
