G = [ [int(d) for d in _.split()] for _ in open(0).read().splitlines()]

def way1(G) -> int:
    dr=[-1,0,1, 0]
    dc=[ 0,1,0,-1]
    R, C = len(G), len(G[0])
    seen=set()
    res = 0
    N = 0
    def DFS(r,c,current) -> int:
        if -1 < r < R and -1 < c < C and G[r][c] != 0 and (r,c) not in seen:
            seen.add( (r,c) )
            current += G[r][c]
            for i in range(4):
                current = DFS(r + dr[i], c + dc[i], current)
        return current
    for r in range(R):
        for c in range(C):
            if G[r][c] != 0 and (r,c) not in seen:
                res += DFS(r, c, 0)
                N += 1
    return res//N

def way2(G) -> int:
    dr=[-1,0,1, 0]
    dc=[ 0,1,0,-1]
    R, C = len(G), len(G[0])
    seen=set()
    res = 0
    N = 0
    def DFS_2(r,c) -> int:
        if -1 < r < R and -1 < c < C and G[r][c] != 0 and (r,c) not in seen:
            seen.add( (r,c) )
            curr = G[r][c]
            for i in range(4):
                curr += DFS_2( r + dr[i], c + dc[i] )
            return curr
        return 0
    for r in range(R):
        for c in range(C):
            if G[r][c] != 0 and (r,c) not in seen:
                res += DFS_2(r, c)
                N += 1
    return res//N

res = way1(G)
res2 = way2(G)

assert res == res2
assert res in [ 33 ]
print(res)
