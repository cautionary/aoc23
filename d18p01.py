inputdata = open('d18i01.txt', 'r')
lines = inputdata.readlines()

maxj = 0
minj = 0
edges = {0: [0]}
pos = 0j
for line in lines:
    (direc, num, color) = line.strip().split()
    num = int(num)
    for i in range(num):
        if direc == 'R':
            pos += 1j
        elif direc == 'D':
            pos += 1+0j
        elif direc == 'L':
            pos -= 1j
        elif direc == 'U':
            pos += -1+0j
        if int(pos.real) not in edges:
            edges[int(pos.real)] = []
        edges[int(pos.real)].append(int(pos.imag))
        maxj = max(maxj, int(pos.imag))
        minj = min(minj, int(pos.imag))
total = 0
for r in range(min(edges), max(edges)+1):
    groups = []
    inside = False
    for c in range(minj, maxj+2):
        if c in edges[r]:
            if not inside:
                gstart = c
                inside = True
        else:
            if inside:
                gend = c-1
                if gstart == gend:
                    groups.append((gstart, gend))
                elif (not (r-1 in edges and gstart in edges[r-1] and gend in edges[r-1])
                      and not (r+1 in edges and gstart in edges[r+1] and gend in edges[r+1])):
                    groups.append((gstart, gend))
                inside = False
            
    if len(groups) == 1:
        groups = []
    for c in range(minj, maxj+1):
        if c in edges[r]:
            char = '#'
            total += 1
        else:
            gloc = 0
            for i, group in enumerate(groups):
                if c > group[1]:
                    gloc += 1
            if gloc % 2 == 1:
                char = '.'
                total += 1
            else:
                char = ' '
                
        print(char, end='')
    print()
        
print(total)
