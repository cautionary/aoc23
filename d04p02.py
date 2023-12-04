infile = open('d04i01.txt', 'r')
lines = infile.readlines()


cards = []
for line in lines:
    matches = 0
    cardpoints = 0
    winners = line.split(':')[1].split('|')[0].split()
    mynums = line.split(':')[1].split('|')[1].split()
    for num in mynums:
        if num in winners:
            matches += 1
    cards.append(matches)

num_cards = []
for i in range(len(cards)):
    num_cards.append(1)

for i in range(len(cards)):
    for match in range(cards[i]):
        num_cards[i + 1 + match] += num_cards[i]


print(sum(num_cards))
    
