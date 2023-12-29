G = [[ int(_, 16) for _ in line.split(' ')] for line in open(0).read().splitlines()]

r,c=0,0
R,C=None, None # diffs
for g in G:
    real, check= sum(g[:-1]) % 256, g[-1]
    if real != check:
        R = real - check
        R += 256 if R < 0 else 0
        break
    r += 1
for g in zip(*G):
    real, check = sum(g[:-1]) % 256, g[-1]
    if real != check:
        C = real - check
        C += 256 if C < 0 else 0
        assert(R==C)
        break
    c += 1
res = ( G[r][c] - R ) * G[r][c]
print(res)
assert( res in [297] )

