inputdata = open('d19i01.txt', 'r')
data = inputdata.read().strip().split('\n\n')

workflows = {}
for line in data[0].split('\n'):
    (wf, ruledata) = line.split('{')
    rules = []
    for r in ruledata[0:-1].split(','):
        if ':' in r:
            cat = r[0]
            op = r[1]
            (num, dest) = r[2:].split(':')
            rules.append({'cat': cat, 'op': op, 'num': int(num), 'dest': dest})
        else:
            rules.append({'op': '*', 'dest': r})
            
    workflows[wf] = rules

parts = []
for line in data[1].split('\n'):
    cats = {}
    for catdata in line[1:-1].split(','):
        (cat, val) = catdata.split('=')
        cats[cat] = int(val)
    parts.append(cats)


total = 0
for part in parts:
    wf = 'in'
    while wf not in ['A', 'R']:
        dest = None
        for rule in workflows[wf]:
            if not dest:
                if rule['op'] == '*':
                    dest = rule['dest']
                elif rule['op'] == '<':
                    if part[rule['cat']] < rule['num']:
                        dest = rule['dest']
                elif rule['op'] == '>':   
                    if part[rule['cat']] > rule['num']:
                        dest = rule['dest']

        wf = dest
    if dest == 'A':
        total += part['x'] + part['m'] + part['a'] + part['s']

print(total)
