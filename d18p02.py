inputdata = open('d18i01.txt', 'r')
lines = inputdata.readlines()

pos = 0j
vertices = [0j]
total = 0
for line in lines:
    (_, _, instr) = line.strip().split()
    num = int(instr[2:7], 16)
    direc = instr[7]
    #(direc, num, color) = line.strip().split()
    #num = int(num)
    total += num
    direc = direc.replace('R', '0').replace('D', '1').replace('L', '2').replace('U', '3')
    if direc == '0':
        pos += complex(0, num)
    elif direc == '1':
        pos += complex(num, 0)
    elif direc == '2':
        pos -= complex(0, num)
    elif direc == '3':
        pos -= complex(num, 0)
    vertices.append(pos)
   

s1 = 0
s2 = 0
for i in range(len(vertices) - 1):
    v1 = vertices[i]
    v2 = vertices[i+1] 

    s1 += v1.real * v2.imag
    s2 += v1.imag * v2.real

print(int(abs(s1-s2)/2 + (total/2) + 1))
