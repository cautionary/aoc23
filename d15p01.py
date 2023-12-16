infile = open('d15i01.txt', 'r')
line = infile.read().strip()

total = 0
for step in line.split(','):
    curval = 0
    for char in step:
        curval = ((curval + ord(char)) * 17) % 256
    total += curval

print(total)
