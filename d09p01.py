infile = open('d09i01.txt', 'r')
lines = infile.readlines()

reports =[]
for line in lines:
    report = []
    for num in line.split():
        report.append(int(num))
    reports.append(report)

sum = 0

for report in reports:
    alldifferences = [report]
    allzeros = False
    while not allzeros:
        differences = []
        for i in range(1, len(alldifferences[-1])):
            differences.append(alldifferences[-1][i] - alldifferences[-1][i-1])
        allzeros = True
        for difference in differences:
            if difference != 0:
                allzeros = False
        alldifferences.append(differences)

    for i in range(len(alldifferences)-1, 0, -1):
        alldifferences[i-1].append(alldifferences[i-1][-1] + alldifferences[i][-1])

    sum += alldifferences[0][-1]

print(sum)
