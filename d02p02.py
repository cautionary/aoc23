infile = open('d02i01.txt', 'r')
lines = infile.readlines()

games = {}
for line in lines:
    line = line.strip()
    gamenum = int(line.split(':')[0].split(' ')[1])
    games[gamenum] = {}
    sets = line.split(':')[1].split(';')
    for s in sets:
        cubes = s.split(', ')
        for c in cubes:
            color = c.split()[1]
            num = int(c.split()[0])
            if not color in games[gamenum]:
                games[gamenum][color] = num
            else:
                games[gamenum][color] = max(num, games[gamenum][color])

total = 0

for gamenum, game in games.items():
    power = 1
    for color, num in game.items():
        power = power * num
    total += power

print(total)

