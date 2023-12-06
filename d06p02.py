infile = open('d06i01.txt', 'r')
lines = infile.readlines()

time = int(lines[0].split(':')[1].replace(" ", ""))
distance = int(lines[1].split(':')[1].replace(" ", ""))

wins = 0
i = 1
firstwin = 0
while not firstwin:
    mydistance = i * (time - i)
    if mydistance > distance:
        firstwin = i
    i += 1
print(time - (firstwin * 2) + 1)
