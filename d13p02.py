infile = open('d13i01.txt', 'r')
data = infile.read()

patterns = data.strip().split("\n\n")

total = 0

def getmatches(lines, omatch):
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

        if foundmatch and match != omatch:
            return match
    return None

notfound = 0
opposite = {'.': '#', '#': '.'}
for pattern in patterns:
    lines = pattern.split('\n')
    foundsmudge = False
    translines = []
    for i in range(len(lines[0])):
        nl = ""
        for line in lines:
            nl += line[i]
        translines.append(nl)
    ohmatch = getmatches(lines, None) 
    ovmatch = getmatches(translines, None)

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if not foundsmudge:
                lines = pattern.split('\n')
                lines[r] = lines[r][0:c] + opposite[lines[r][c]] + lines[r][c+1:]
                translines = []
                for i in range(len(lines[0])):
                    nl = ""
                    for line in lines:
                        nl += line[i]
                    translines.append(nl)
                hmatch = getmatches(lines, ohmatch) 
                vmatch = getmatches(translines, ovmatch)
                if hmatch != None:
                    total += (hmatch + 1) * 100
                    foundsmudge = True
                elif vmatch != None:
                    total += vmatch + 1
                    foundsmudge = True

print(total)
