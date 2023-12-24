from collections import defaultdict

inputdata = open('d23i01.txt', 'r')
lines = inputdata.readlines()

start = complex(0, lines[0].index('.'))
end = complex(len(lines) -1, lines[-1].index('.'))


def topological_sort(graph):
    visited = set()
    sorted_nodes = []

    def visit(node):
        if node not in visited:
            visited.add(node)
            for successor in graph[node]:
                visit(successor)
            sorted_nodes.append(node)

    for node in graph:
        visit(node)

    return sorted_nodes[::-1]

def longest_path(graph, weights):
    sorted_nodes = topological_sort(graph)
    dist = defaultdict(lambda: float('-inf'))
    dist[sorted_nodes[0]] = 0

    for node in sorted_nodes:
        for successor in graph[node]:
            dist[successor] = max(dist[successor], dist[node] + weights[(node, successor)])

    return max(dist.values())




vertices = {start, end}
slopes = {}


pathtiles = {start, end}
for r in range(1, len(lines) - 1):
    for c in range(len(lines[0])):
        if lines[r][c] in ['.', '<', 'v', '^', '>']:
            pathtiles.add(complex(r,c))
            if lines[r][c] != '.':
                slopes[complex(r,c)] = lines[r][c]



for pos in pathtiles:
    n = []
    for d in [-1j, 1j, -1+0j, 1+0j]:
        npos = pos + d
        if npos in pathtiles:
            n.append(npos)
    if len(n) > 2:
        vertices.add(pos)


connections = {}
graph = {}
weights = {}

for vertex in vertices:
    connections[vertex] = {}
    graph[vertex] = []
    n = {}
    for d in [-1j, 1j, -1+0j, 1+0j]:
        npos = vertex + d
        if npos in pathtiles:
            if not (npos in slopes and
                    (d == 1j and slopes[npos] == '<' or
                    d == -1j and slopes[npos] == '>' or
                    d == 1+0j and slopes[npos] == '^' or
                    d == -1+0j and slopes[npos] == 'v')):
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
                        connections[vertex][np] = count
                        graph[vertex].append(np)
                        weights[(vertex, np)] = count
                        foundend = True
                    elif (np in slopes and
                            (di == 1j and slopes[np] == '<' or
                            di == -1j and slopes[np] == '>' or
                            di == 1+0j and slopes[np] == '^' or
                            di == -1+0j and slopes[np] == 'v')):
                        foundend = True
                    else:
                        nnp = np
                        di = d
            pos = nnp 

graph[end] = []

print(longest_path(graph, weights))


#2481 too high
