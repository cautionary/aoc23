from math import lcm

infile = open('d08i01.txt', 'r')
lines = infile.readlines()

instructions = lines[0].strip().replace("L", "0").replace("R", "1")

network = {}
for line in lines[2:]:
    network[line[0:3]] = (line[7:10], line[12:15])

nodes = []
for node in network:
    if node[2] == 'A':
        nodes.append(node)

node_lengths = []

found_lengths = False
count = 0
while not found_lengths:
    for i, node in enumerate(nodes):
        if nodes[i][2] != 'Z':
            nodes[i] = network[node][int(instructions[count % len(instructions)])]
            if nodes[i][2] == 'Z':
                node_lengths.append( count + 1)
    if len(node_lengths) == len(nodes):
        found_lengths = True

    count += 1

print(lcm(*node_lengths))

