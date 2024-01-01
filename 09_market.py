G = [_.strip() for _ in open(0).read().splitlines()]

R,C = len(G), len(G[0])
sr = 0
er = R - 1
sc = ec = None
for i in range(C):
    if G[0][i] == ' ':
        sc = i
    if G[-1][i] == ' ':
        ec = i

seen = { (sr, sc) }
D = [ (sr, sc, 1) ]
DR=[1,0,-1,0]
DC=[0,-1,0,1]

res = None
while D:
    r, c, steps = D.pop(0)
    if r == er and c == ec:
        res = steps
        break
    for i in range(4):
        rr = r + DR[i]
        cc = c + DC[i]
        if not -1 < rr < R or not -1 < cc < C or (rr,cc) in seen or G[rr][cc] == '#':
            continue
        D.append( (rr, cc, steps+1) )
        seen.add( (rr, cc) )


print(res)
assert res in [ 6723 ]
