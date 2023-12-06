infile = open('d06i01.txt', 'r')
lines = infile.read()

races = []
for i in range(1, len(lines.split('\n')[0].split())):
    races.append({"time": int(lines.split('\n')[0].split()[i]), "distance": int(lines.split('\n')[1].split()[i])})


product = 1

for race in races:
    wins = 0
    for i in range(1, race["time"]):
        mydistance = i * (race["time"] - i)
        if mydistance > race["distance"]:
            wins += 1
    product *= wins

print(product)
