infile = open('d03i01.txt', 'r')
lines = infile.readlines()

part_locs = []
part_nums = []
i = 0
for line in lines:
    part_num = ""
    neighbors = []
    j = 0
    line = line.strip()
    for c in line:
        if c.isnumeric():
            part_num = part_num + c
            for r in range(i-1, i+2):
                for c in range(j-1, j+2):
                    if (i,j) != (r,c) and r >= 0 and c >= 0 and r <= len(lines) + 1 and c <= len(line) + 1:
                        neighbors.append(complex(r,c))
        elif not c.isnumeric(): 
            if part_num:
                part_nums.append({"part_num": int(part_num), "neighbors": neighbors})
                part_num = ""
                neighbors = []

            if c != '.':
                part_locs.append(complex(i, j))
        j += 1
    if part_num:
        part_nums.append({"part_num": int(part_num), "neighbors": neighbors})
    i += 1

total = 0
for part_num in part_nums:
    is_valid = False
    pnum = part_num["part_num"]
    for neighbor in part_num["neighbors"]:
        if neighbor in part_locs:
            is_valid = True

    if is_valid:
        total += pnum

print(total)

