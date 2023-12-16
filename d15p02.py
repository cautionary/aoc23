infile = open('d15i01.txt', 'r')
line = infile.read().strip()

boxes = [{} for _ in range(256)]
for step in line.split(','):
    box = 0
    for char in step:
        if char.isalpha():
            box = ((box + ord(char)) * 17) % 256
    if '=' in step:
        (label, fl) = (step.split('=')[0], int(step.split('=')[1]))
        boxes[box][label] = fl
    else:
        label = step.split('-')[0]
        fl = None
        if label in boxes[box]:
            del(boxes[box][label])
total = 0
for i, box in enumerate(boxes):
    if box:
        j = 1
        for lens in box:
            fl = box[lens]
            power = (i + 1) * j * fl
            total += power
            j += 1
        

print(total)

