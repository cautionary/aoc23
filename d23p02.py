inputdata = open('d23i01.txt', 'r')
lines = inputdata.readlines()

start = complex(0, lines[0].index('.'))
end = complex(len(lines) -1, lines[-1].index('.'))

vertices = {start, end}
pathtiles = {start, end}
for r in range(1, len(lines) - 1):
    for c in range(len(lines[0])):
        if lines[r][c] in ['.', '<', 'v', '^', '>']:
            pathtiles.add(complex(r,c))

for pos in pathtiles:
    n = []
    for d in [-1j, 1j, -1+0j, 1+0j]:
        npos = pos + d
        if npos in pathtiles:
            n.append(npos)
    if len(n) > 2:
        vertices.add(pos)

graph = {}
weights = {}

for vertex in vertices:
    graph[vertex] = []
    n = {}
    for d in [-1j, 1j, -1+0j, 1+0j]:
        npos = vertex + d
        if npos in pathtiles:
            n[npos] = d

    for pos in n:
        di = n[pos]
        #print(vertex, pos, di)
        visited = {vertex}
        count = 1
        foundend = False
        while not foundend:
            #print(vertex, pos, di)
            visited.add(pos)
           
            for d in [-1j, 1j, -1+0j, 1+0j]:
                np = pos + d
                #print('testing',vertex, pos, np)
                if np in pathtiles and np not in visited:
                    count += 1
                    if np in vertices:
                        foundend = True
                        if np != start:
                            graph[vertex].append(np)
                            weights[(vertex, np)] = count
            
                    else:
                        nnp = np
                        di = d
            pos = nnp 

def traverse(v, pos, weight, count):
    count += weight
    v.add(pos)
    if pos == end:
        return(count)
    answers = []
    nexts = [x for x in graph[pos] if x not in v]
    if nexts:
        for next in nexts:
            answers.append(traverse(v.copy(), next, weights[(pos, next)], count))
        return max(answers)
    else:
        return 0

 

print(traverse(set(), start, 0, 0))

#6898
