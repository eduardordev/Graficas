lines = []

with open("carpet.txt") as f:
    for line in f:
        #if line.startswith('vt'):
        #    line = line[:-2] + ' 0.000\n'
        if line.startswith('f'):
            line = line[:-2] + '\n'
        lines.append(line)

with open('readme.txt', 'w') as f:
    for line1 in lines:
        f.write(line1)

