infile = open('d11i01.txt', 'r')
lines = infile.readlines()

multiplier = 1000000

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


galaxies = set()
for i, line in enumerate(lines):
    for j, c in enumerate(line.strip()):
        if c == '#':
            rowc = 0
            for row in emptyrows:
                if row < i:
                    rowc += 1
            colc = 0
            for col in emptycols:
                if col < j:
                    colc += 1
            galaxies.add(complex(rowc * (multiplier-1) + i, colc * (multiplier-1) + j))

pairs = set()
total = 0
for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if (galaxy1, galaxy2) not in pairs and (galaxy2, galaxy1) not in pairs:
            total += abs(galaxy1.real - galaxy2.real) + abs(galaxy1.imag - galaxy2.imag)
            pairs.add((galaxy1, galaxy2))

print(int(total))

