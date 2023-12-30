lines = [list(map(int, line.split(' '))) for line in open (0).read().splitlines()]

seen=set()
R = C = 100# 10 # test
R, C = 100000, 20000 # real
i = 0
# we iterate twice - 1st iter : get gcd of row & col respectively
import math
rows, cols = [], []
for i, line in enumerate(lines):
    sc, sr, dc, dr = line
    rows += [sr, dr]
    cols += [sc, dc]
gcd_rows = math.gcd( *rows )
gcd_cols = math.gcd( *cols )

# 2st iter : shrink space by the gcd of rows/cols
R //= gcd_rows
C //= gcd_cols
for i, line in enumerate(lines):
    sc, sr, dc, dr = line
    sr, dr = map(lambda x:x//gcd_rows, (sr,dr))
    sc, dc = map(lambda x:x//gcd_cols, (sc,dc))
    er = min(R, sr + dr)
    ec = min(C, sc + dc)
    # print(i, '/', sc, sr, dc, dr)
    for r in range(sr, er):
        for c in range(sc, ec):
            seen.add( (r,c) )

gcd_mult = gcd_rows*gcd_cols
res = (R*C - len(seen)) * gcd_mult

print(res)
assert res in [ 154807700 ]

"""
def dbg(R,C):
    for g in [['.' if (r,c) not in seen else 'x' for c in range(C)] for r in range(R)]:
        print(''.join(g))
dbg(R,C)
"""
