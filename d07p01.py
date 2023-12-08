infile = open('d07i01.txt', 'r')
lines = infile.readlines()

hands = []
for line in lines:
    hand = line.split()[0].replace("T", "B").replace("J", "C").replace("Q", "D").replace("K", "E").replace("A", "F")
    bid = int(line.split()[1])
    hands.append((hand, bid))
    

def compare_hands(h1, h2):
    #Types: 5ooK -> 6, 4ooK -> 5, FH -> 4, 3ooK -> 3, 2P -> 2, 1P -> 1, HC -> 0
    hcs = []
    for _ in range(2):
        hcs.append({'2': 0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F': 0})

    for c in h1:
        hcs[0][c] += 1
    for c in h2:
        hcs[1][c] += 1

    hccs = [[],[]]
    hss = [0, 0]
    for i in range(2):
        for c in hcs[i]:
            if hcs[i][c] > 0:
                hccs[i].append(hcs[i][c])
        if 5 in hccs[i]:
            hss[i] = 6
        elif 4 in hccs[i]:
            hss[i] = 5
        elif 3 in hccs[i] and 2 in hccs[i]:
            hss[i] = 4
        elif 3 in hccs[i]:
            hss[i] = 3
        elif hccs[i].count(2) > 1:
            hss[i] = 2
        elif 2 in hccs[i]:
            hss[i] = 1
        else:
            hss[i] = 0

    if hss[0] > hss[1]:
        return True
    elif hss[0] < hss[1]:
        return False
    elif h1 > h2:
        return True
    else:
        return False

def sort_hands(hands):
    n = len(hands)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if compare_hands(hands[j][0], hands[j+1][0]):
                hands[j], hands[j+1] = hands[j+1], hands[j]
                already_sorted = False
        if already_sorted:
            break
    return(hands)

hands = sort_hands(hands)
answer = 0
for i, hand in enumerate(hands):
    answer += (i+1) * hand[1]

print(answer)
