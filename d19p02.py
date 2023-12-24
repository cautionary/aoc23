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


groups = [({'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1,4000)}, 'in')]

accepted = []
rejected = []
while groups:
    (group, wf) = groups.pop(0)
    matched = False
    for rule in workflows[wf]:
        if not matched:
            if rule['op'] == '*':
                if rule['dest'] == 'A':
                    accepted.append(group)
                elif rule['dest'] != 'R':
                    groups.append((group, rule['dest']))
                else:
                    rejected.append(group)
            elif rule['op'] == '<':
                if group[rule['cat']][0] < rule['num'] and group[rule['cat']][1] >= rule['num']: 
                    matched = True
                    g1 = group.copy()
                    g1[rule['cat']] = (group[rule['cat']][0], rule['num'] - 1)
                    if rule['dest'] == 'A':
                        accepted.append(g1)
                    elif rule['dest'] != 'R':
                        groups.append((g1, rule['dest']))
                    else:
                        rejected.append(g1)
                    g2 = group.copy()
                    g2[rule['cat']] = (rule['num'], group[rule['cat']][1])
                    groups.append((g2, wf))
                elif group[rule['cat']][1] < rule['num']:
                    matched = True
                    if rule['dest'] == 'A':
                        accepted.append(group)
                    elif rule['dest'] != 'R':
                        groups.append((group, rule['dest']))
                    else:
                        rejected.append(group)
            elif rule['op'] == '>':
                if group[rule['cat']][0] <= rule['num'] and group[rule['cat']][1] > rule['num']: 
                    matched = True
                    g1 = group.copy()
                    g1[rule['cat']] = (group[rule['cat']][0], rule['num'])
                    groups.append((g1, wf))
                    g2 = group.copy()
                    g2[rule['cat']] = (rule['num'] + 1, group[rule['cat']][1])
                    if rule['dest'] == 'A':
                        accepted.append(g2)
                    elif rule['dest'] != 'R':
                        groups.append((g2, rule['dest']))
                    else:
                        rejected.append(g2)
                elif group[rule['cat']][0] > rule['num']:
                    matched = True
                    if rule['dest'] == 'A':
                        accepted.append(group)
                    elif rule['dest'] != 'R':
                        groups.append((group, rule['dest']))
                    else:
                        rejected.append(group)


            

total = 0
for group in accepted:
    prod = 1
    for cat in ['x', 'm', 'a', 's']:
        prod *= (group[cat][1] - group[cat][0] + 1)

    total += prod

print(total)
