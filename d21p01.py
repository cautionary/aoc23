inputdata = open('d21i01.txt', 'r')
lines = inputdata.readlines()

height = len(lines)
width = len(lines[0].strip())

rocks = set()

for r in range(height):
    for c in range(width):
        if lines[r][c] == 'S':
            start = complex(r,c)
        elif lines[r][c] == '#':
            rocks.add(complex(r,c))

steps = 64
positions = {start}
for i in range(steps):
    newpos = set()
    for pos in positions:
        for n in [pos + 1j, pos - 1j, pos + 1+0j, pos - 1+0j]:
            if n not in rocks:
                newpos.add(n)

    positions = newpos.copy()


#    for r in range(height):
#        for c in range(width):
#            if complex(r,c) in rocks:
#                char = '#'
#            elif complex(r,c) in positions:
#                char = 'O'
#            else:
#                char = '.'
#            print(char, end='')
#        print()
#    print()

print(len(positions))
