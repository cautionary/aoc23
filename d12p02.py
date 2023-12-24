import functools

@functools.cache
def check(cond, counts):
    if not counts:
        if '#' in cond:
            return 0
        else:
            return 1
    if not cond:
        if not counts:
            return 1
        else:
            return 0
 
    result = 0

    if cond[0] == '?' or cond[0] == '.':
        result += check(cond[1:], counts)        

    if cond[0] == '?' or cond[0] == '#':
        if (counts[0] <= len(cond)
            and '.' not in cond[0:counts[0]]
            and (counts[0] == len(cond) or cond[counts[0]] != "#")):
            result += check(cond[counts[0] + 1 :], counts[1:])

    return result

inputdata = open('d12i01.txt', 'r')
lines = inputdata.readlines()

lines = [line.strip() for line in lines]


total = 0
for line in lines:
    cond = line.split()[0]

    for i in range(4):
        cond += "?" + line.split()[0]
   
    counts = []
    for i in range(5):
        for n in line.split()[1].split(','):
            counts.append(int(n))
    result = check(cond, tuple(counts))
    total += result

print(total)
