infile = open('d04i01.txt', 'r')
lines = infile.readlines()

points = 0
for line in lines:
    matches = 0
    cardpoints = 0
    winners = line.split(':')[1].split('|')[0].split()
    mynums = line.split(':')[1].split('|')[1].split()
    for num in mynums:
        if num in winners:
            matches += 1
    if matches == 1:
        cardpoints = 1
    elif matches > 1:
        cardpoints = 2 ** (matches - 1)
    points += cardpoints

print(points)
