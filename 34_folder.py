# 103879262
from collections import defaultdict
parts = open('34.1').read().split('Folder: ')[1:]
for i, part in enumerate(parts):
    #print('/part', part, '/len', len(part))
    parts[i] = part.splitlines()
    parts[i][0] = int( parts[i][0] )
    #print('/parts[i][1:]', parts[i][1:])
    for j in range(1, len(parts[i])):
        parts[i][j] = parts[i][j][3:]
D = defaultdict( lambda: defaultdict(list) )
for i, lines in enumerate(parts):
    #print("/i", i)
    #for l in part:print(l)
    n = lines[0]
    for line in lines[1:]:
        if 'temporary' in line.lower():
            D[n]['temp'].append(line)
        elif 'delete' in line.lower():
            D[n]['dele'].append(line)
        else:
            D[n]['none'].append(line)
for key, data in D.items():
    # dbg
    print('/Folder', key)
    for k, d in data.items():
        print('/key', k)
        for line in d: print('\t',line)
        print()
    print('--')

tt4 = 0
for k,d in D[4].items():
    for line in d:
        tt4 += int(line.split()[1])
print('/tt4', tt4)
tt0to3 = 0
for i in range(4):
    for k,d in D[i].items():
        for line in d:
            if 'delete' in line.lower():
                tt0to3 += int(line.split()[1])
            if 'temp' in line.lower():
                if 'folder' not in line.lower():
                    tt0to3 += int(line.split()[1])
                # elif # how? i dont understand

print('/tt0to3', tt0to3)
print('/attempt', tt4 + tt0to3)
print('/tomatch', 103879262)

