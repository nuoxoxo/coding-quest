G = [ [int(d) for d in _.split(' ')] for _ in open(0).read().splitlines()]

dr=[-1,0,1, 0]
dc=[ 0,1,0,-1]
R, C = len(G), len(G[0])
seen=set()
res = 0
N = 0

def DFS(r,c) -> int:
    if -1 < r < R and -1 < c < C and G[r][c] != 0 and (r,c) not in seen:
        seen.add( (r,c) )
        curr = G[r][c]
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            curr += DFS(rr, cc)
        return curr
    return 0

for r in range(R):
    for c in range(C):
        if G[r][c] != 0 and (r,c) not in seen:
            res += DFS(r, c)
            N += 1

print(res//N)
assert(res//N in [33])
