U, D = open('32.0').read().split('\n\n')
lines = [_.split() for _ in U.splitlines()]
R, C = len(lines), len(lines[1])
head = [''] + lines[0]
adj = {}
for r in range(1, R):
    col = lines[r][0]
    for c in range(1, C):
        row = head[c]
        name = col+row
        adj[ name ] = int(lines[r][c])

for k,v in adj.items():print('/dict',k,v)

lines = [_.split(':') for _ in D.splitlines()]
dist = []
for line in lines:
    idx = line[0].split()[1]
    names = [_.strip() for _ in line[1].split('->')]
    temp = 0
    for i in range(len(names) - 1):
        name = names[i] + names[i+1]
        temp += adj[name]
    dist.append(temp)

res = sum(dist)
print(dist)
print('/res', res)

assert res in [ 353480, 6979629 ]
