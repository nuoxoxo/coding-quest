lines = [[float(_) for _ in line.split()] for line in open(0).read().splitlines()]

def find( lines, bound, t, window ):
    S = set()
    for i in range( bound ):
        for j in range( bound ):
            S.add((i,j))
    for c, r, dc, dr in lines:
        sr = dr * t + r
        sc = dc * t + c
        for sec in range( window + 1 ):
            R = dr * sec + sr
            C = dc * sec + sc
            R,C=int(R),int(C)
            if -1 < R < bound and -1 < C < bound:
                S.discard((R,C))
        #print('S/',S)
    assert len(S) == 1
    return ':'.join(list(map(str, list(S.pop())[::-1])))

Bound = 100#8
T = 3600
Window = 60

res = find( lines, Bound, T, Window )
print('res/',res)
assert res=='5:8'
