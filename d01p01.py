infile = open('d01i01.txt', 'r')
lines = infile.readlines()

nums = []
for line in lines:
    linenums = []
    for char in line:
        if char >= "0" and char <= "9":
            linenums.append(char)
    nums.append(int(linenums[0]+linenums[-1]))

print(sum(nums))
