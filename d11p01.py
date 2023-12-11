infile = open('d11s01.txt', 'r')
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

print(emptyrows, emptycols)
