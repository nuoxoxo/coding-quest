# 103879262
from collections import defaultdict
import json
parts = open('34.0').read().split('Folder: ')[1:]
res = 0
for i, part in enumerate(parts):
    #print('/part', part, '/len', len(part))
    parts[i] = part.splitlines()
    parts[i][0] = int( parts[i][0] )
    #print('/parts[i][1:]', parts[i][1:])
    for j in range(1, len(parts[i])):
        parts[i][j] = parts[i][j][3:]
        if 'fold' not in parts[i][j].split()[1].lower():
            res += int(parts[i][j].split()[1])
D = defaultdict( lambda: defaultdict(list) )
for i, lines in enumerate(parts):
    #print("/i", i)
    #for l in part:print(l)
    n = lines[0]
    for line in lines[1:]:
        D[n]['entire?'] = [False]
        if 'temporary' in line.lower():
            D[n]['temp'].append(line)
        elif 'delete' in line.lower():
            D[n]['dele'].append(line)
        else:
            D[n]['none'].append(line)

def markDoomedFolder(line: str) -> None:
    if 'FOLDER' in line:
        n = int(line.split()[-1][:-1])
        global D
        if not D[n]['entire?'][0]:
            mod = True
        D[n]['entire?'][0] = True

# nested folders
mod = True
while mod:
    mod = False
    for _, data in D.items():
        # destroy-all
        if data['entire?'][0]:
            for line in data['none']:
                markDoomedFolder(line)
                # if 'FOLDER' in line:
                #     n = int(line.split()[-1][:-1])
                #     if not D[n]['entire?'][0]:
                #         mod = True
                #     D[n]['entire?'][0] = True
            for line in data['temp']:
                markDoomedFolder(line)
                # if 'FOLDER' in line:
                #     n = int(line.split()[-1][:-1])
                #     if not D[n]['entire?'][0]:
                #         mod = True
                #     D[n]['entire?'][0] = True
            for line in data['dele']:
                markDoomedFolder(line)
                # if 'FOLDER' in line:
                #     n = int(line.split()[-1][:-1])
                #     if not D[n]['entire?'][0]:
                #         mod = True
                #     D[n]['entire?'][0] = True
        # not destroy-all
        else:
            for line in data['temp']:
                markDoomedFolder(line)
                # if 'FOLDER' in line:
                #     n = int(line.split()[-1][:-1])
                #     if not D[n]['entire?'][0]:
                #         mod = True
                #     D[n]['entire?'][0] = True
            for line in data['dele']:
                markDoomedFolder(line)
                # if 'FOLDER' in line:
                #     n = int(line.split()[-1][:-1])
                #     if not D[n]['entire?'][0]:
                #         mod = True
                #     D[n]['entire?'][0] = True

# dbg : look through every Folder
for key, data in D.items():
    print(key, json.dumps(data, indent=2))

def getNoneFolderSize(line: str) -> int:
    if 'FOLDER' not in line:
        print(line, n)
        return int(line.split()[1])
    return 0

# calc
res = 0
for _, data in D.items():
    if data['entire?'][0]:
        for line in data['none']:
            res += getNoneFolderSize(line)
    for line in data['temp']:
        res += getNoneFolderSize(line)
    for line in data['dele']:
        res += getNoneFolderSize(line)
print('/res', res)

assert res in [349035592144, 103879262]
# attempts : 247654027296
