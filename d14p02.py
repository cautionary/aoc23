infile = open('d14s01.txt', 'r')
lines = infile.readlines()

rocks = set()
obstacles = [[-1] for _ in range(len(lines[0].strip()))]

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == 'O':
            rocks.add(complex(r,c))
        elif char =='#':
            obstacles[c].append(r)

rocks_final = set()
for rock in rocks:
    obsinway =([i for i in obstacles[int(rock.imag)] if i < rock.real])
    rocks_final.add(complex(max(obsinway) + 1, rock.imag))
    obstacles[int(rock.imag)].append(max(obsinway) + 1)
        
        
numrows = len(lines)
total = 0
for rock in rocks_final:
    total += (numrows - int(rock.real))

print(total)
