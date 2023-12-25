import networkx as nx
import matplotlib.pyplot as plt

inputdata = open('d25i01.txt', 'r')
lines = inputdata.readlines()

graph = {}

for line in lines:
    comps = line.replace(':', '').split()
    if comps[0] not in graph:
        graph[comps[0]] = []
    for comp in comps[1:]:
        if comp not in graph:
            graph[comp] = []
        graph[comp].append(comps[0])
        graph[comps[0]].append(comp)

G = nx.Graph()


for g in graph:
    for h in graph[g]:
        #if (g, h) not in [('rhh', 'mtc'), ('mtc', 'rhh'), ('tmb', 'gpj'), ('gpj', 'tmb'), ('xtx', 'njn'), ('njn', 'xtx')]:
        G.add_edge(g, h)


centrality = nx.edge_betweenness_centrality(G)
G.remove_edges_from(sorted(centrality, key=centrality.get)[-3:])
components = list(nx.connected_components(G)) 
print(len(components[0]) * len(components[1]))


#nx.draw_networkx(G)
#
#ax = plt.gca()
#ax.margins(0.20)
#plt.axis("off")
#plt.show()
