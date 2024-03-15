from collections import deque

def Solver(G):
    DR, DC = [-1,1,0,0], [0,0,1,-1]
    levels = len(G)
    assert levels == 2
    R, C= len(G[0]), len(G[0][0])
    print('/RC', R, C)
    start, end = (0, 1, 0), (0, R - 2, C - 1)
    Q = deque()
    Q.append( (start, 1) )

    Seen = set()
    Seen.add( (start, 1) )

    while Q:
        pos, res = Q.popleft()
        L, r, c = pos
        # if L == 1 and G[L][r][c] == '$':print('/underground $ -', pos, res)
        # if L == 0 and G[L][r][c] == '$':print('/overground $ -', pos, res)
        if pos == end:
            print(pos, res)
            return res
        for dr, dc in zip(DR, DC):
            rr, cc = r + dr, c + dc
            if not -1 < rr < R or not -1 < cc < C or G[L][rr][cc] == '#':
                continue
            if ((L, rr, cc), res + 1) not in Seen:
                Seen.add(((L, rr, cc), res + 1))
                Q.append(((L, rr, cc), res + 1))
            if G[L][rr][cc] == '$' and ((1 - L, rr, cc), res + 1) not in Seen:
                Seen.add(((1 - L, rr, cc), res + 1))
                Q.append(((1 - L, rr, cc), res + 1))

    return -1

G = [_.splitlines() for _ in open('36.1').read().split('\n\n')]
for g in G:
    for gg in g:print(gg)
    print()
res = Solver(G)
print('/test', res)
# assert res == 53

G = [_.splitlines() for _ in open('36.0').read().split('\n\n')]
res = Solver(G)
print('/real', res)
#assert res == 250

# attempts 258 257 241 251 245
