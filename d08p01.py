infile = open('d08i01.txt', 'r')
lines = infile.readlines()

instructions = lines[0].strip().replace("L", "0").replace("R", "1")

network = {}
for line in lines[2:]:
    network[line[0:3]] = (line[7:10], line[12:15])

node = 'AAA'
count = 0
while node != "ZZZ":
    node = network[node][int(instructions[count % len(instructions)])]
    count += 1

print(count)

