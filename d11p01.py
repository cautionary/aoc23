infile = open('d11i01.txt', 'r')
lines = infile.readlines()

emptyrows = []
emptycols = []
for i, line in enumerate(lines):
    line = line.strip()
    if line.count('.') == len(line):
        emptyrows.append(i)

for i in range(len(lines[0])):
    isempty = True
    for line in lines:
        if line[i] != '.':
            isempty = False
    if isempty:
        emptycols.append(i)

emptyrows.reverse()
for i in emptyrows:
    lines.insert(i, lines[i])

emptycols.reverse()
for i in emptycols:
    for j in range(len(lines)):
        lines[j] = lines[j][0:i] + '.' + lines[j][i:]

galaxies = set()
for i, line in enumerate(lines):
    for j, c in enumerate(line.strip()):
        if c == '#':
            galaxies.add(complex(i,j))

pairs = set()
total = 0
for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if (galaxy1, galaxy2) not in pairs and (galaxy2, galaxy1) not in pairs:
            total += abs(galaxy1.real - galaxy2.real) + abs(galaxy1.imag - galaxy2.imag)
            pairs.add((galaxy1, galaxy2))

print(int(total))
