infile = open('d01i01.txt', 'r')
lines = infile.readlines()

numwords = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
        }

nums = []
for line in lines:
    firstfound = False
    linenums = []
    i = 0
    while not firstfound:
        if line[i] >= "0" and line[i] <= "9":
            linenums.append(line[i])
            firstfound = True

        else:
            for k, v in numwords.items():
                if line[i:i+len(k)] == k:
                    linenums.append(v)
                    firstfound = True
        i += 1

    lastfound = False
    i = 1
    while not lastfound:
        s = len(line) - i
        if line[s] >= "0" and line[s] <= "9":
            linenums.append(line[s])
            lastfound = True
        else:
            for k, v in numwords.items():
                if i >= len(k) and line[s:s+len(k)] == k:
                    linenums.append(v)
                    lastfound = True
        i += 1

    nums.append(int(linenums[0]+linenums[-1]))

print(sum(nums))
