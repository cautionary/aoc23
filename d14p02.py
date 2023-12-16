import functools
infile = open('d14i01.txt', 'r')
lines = infile.readlines()
numrows = len(lines)


def transpose_obstacles(obstacles):
    tobs = [[-1,] for _ in range(len(lines))]
    for row, obs in enumerate(obstacles):
        for ob in obs:
            if ob not in [-1, len(lines[0].strip())]:
                tobs[ob].append(row)
    for i in range(len(tobs)):
        tobs[i].append(len(lines))
    return tobs

def getreal(x):
    return(x.real)

def getimag(x):
    return(x.imag)

rocks = set()
obstacles = [[-1] for _ in range(len(lines[0].strip()))]

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == 'O':
            rocks.add(complex(r,c))
        elif char =='#':
            obstacles[c].append(r)

for i in range(len(obstacles)):
    obstacles[i].append(len(lines))
obstacles_t = transpose_obstacles(obstacles)
rock_history = []
#rocks_final = set()

while rocks not in rock_history:
    rock_history.append(rocks.copy())
    print(len(rock_history))

    #Roll north
    for i in range(len(lines)):
        for j in range(len(obstacles[i]) - 1):
            seg_rocks = [r for r in rocks if r.imag == i and r.real > obstacles[i][j] and r.real < obstacles[i][j+1]]
            for sr in seg_rocks:
                rocks.remove(sr)
            for k in range(len(seg_rocks)):
                rocks.add(complex(obstacles[i][j] + 1 + k, i))
        
    for i in range(len(lines)):
        for j in range(len(obstacles_t[i]) -1):
            seg_rocks = [r for r in rocks if r.real == i and r.imag > obstacles_t[i][j] and r.imag < obstacles_t[i][j+1]]
            for sr in seg_rocks:
                rocks.remove(sr)
            for k in range(len(seg_rocks)):
                rocks.add(complex(i, obstacles_t[i][j] + 1 + k))


    for i in range(len(lines)):
        for j in range(len(obstacles[i])-1, 0, -1):
            seg_rocks = [r for r in rocks if r.imag == i and r.real < obstacles[i][j] and r.real > obstacles[i][j-1]]
            for sr in seg_rocks:
                rocks.remove(sr)
            for k in range(len(seg_rocks)):
                rocks.add(complex(obstacles[i][j] - 1 - k, i))

    for i in range(len(lines)):
        for j in range(len(obstacles_t[i]) -1, 0, -1):
            seg_rocks = [r for r in rocks if r.real == i and r.imag < obstacles_t[i][j] and r.imag > obstacles_t[i][j-1]]
            for sr in seg_rocks:
                rocks.remove(sr)
            for k in range(len(seg_rocks)):
                rocks.add(complex(i, obstacles_t[i][j] - 1 - k))
        

#    for rock in sorted(rocks, key=getreal):
#        obsinway =([i for i in obstacles[int(rock.imag)] if i < rock.real])
#        rocks_final.add(complex(max(obsinway) + 1, rock.imag))
#        obstacles[int(rock.imag)].remove(int(rock.real))
#        obstacles[int(rock.imag)].append(max(obsinway) + 1)
#    rocks = rocks_final.copy()
#    rocks_final.clear()
#    #Roll west
#    obstacles = transpose_obstacles(obstacles)
#    for rock in sorted(rocks, key=getimag):
#        obsinway =([i for i in obstacles[int(rock.real)] if i < rock.imag])
#        rocks_final.add(complex(rock.real, max(obsinway) +1))
#        obstacles[int(rock.real)].remove(int(rock.imag))
#        obstacles[int(rock.real)].append(max(obsinway) + 1)
#    rocks = rocks_final.copy()
#    rocks_final.clear()
#    #Roll south
#    obstacles = transpose_obstacles(obstacles)
#    for rock in sorted(rocks, key=getreal, reverse=True):
#        obsinway =([i for i in obstacles[int(rock.imag)] if i > rock.real])
#        rocks_final.add(complex(min(obsinway) - 1, rock.imag))
#        obstacles[int(rock.imag)].remove(int(rock.real))
#        obstacles[int(rock.imag)].append(min(obsinway) - 1)
#    rocks = rocks_final.copy()
#    rocks_final.clear()
#    #Roll east
#    obstacles = transpose_obstacles(obstacles)
#    for rock in sorted(rocks, key=getimag, reverse=True):
#        obsinway =([i for i in obstacles[int(rock.real)] if i > rock.imag])
#        rocks_final.add(complex(rock.real, min(obsinway) -1))
#        obstacles[int(rock.real)].remove(int(rock.imag))
#        obstacles[int(rock.real)].append(min(obsinway) -1)
#    rocks = rocks_final.copy()
#    rocks_final.clear()
#    obstacles = transpose_obstacles(obstacles)
        
        
        
#100839 too low
#100876 answer
