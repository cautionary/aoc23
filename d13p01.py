infile = open('d13i01.txt', 'r')
data = infile.read()

patterns = data.strip().split("\n\n")

total = 0

def getmatches(lines):
    matches = []
    for i in range(len(lines)-1):
        if lines[i] == lines[i+1]:
            matches.append(i)
    for match in matches:
        foundmatch = True
        i = match
        j = match + 1
        while i >= 0 and j < len(lines):
            if lines[i] != lines[j]:
                foundmatch = False
            i -= 1
            j += 1

        if foundmatch:
            return match
    return None

for pattern in patterns:
    lines = pattern.split('\n')
    translines = []
    for i in range(len(lines[0])):
        nl = ""
        for line in lines:
            nl += line[i]
        translines.append(nl)
    hmatch = getmatches(lines) 
    vmatch = getmatches(translines)
    if hmatch != None:
        total += (hmatch + 1) * 100
    else:
        total += vmatch + 1

print(total)

