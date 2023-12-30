lines = open(0).read().splitlines()

from collections import defaultdict

D = defaultdict(int)
cmp = False
res = []

def rvalue(R) :
    return int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]

i = 0

while True:
    #print('Nr/',i)
    expr = lines[i].split(' ')
    CMD = expr[0]
    assert len (expr) in [1,2,3]
    if len(expr) == 1: # END
        break
    elif len(expr) == 2:
        R = rvalue( expr[1] )
        if CMD == 'OUT':
            print('out/', R)
            res.append(R)
        elif CMD == 'JIF' and cmp or CMD == 'JMP':
            i = (i+R) % len(lines)
            continue
    elif len(expr) == 3:
        L, R = expr[1:]
        R = rvalue(R)
        assert isinstance(L, str)
        match CMD:
            case 'MOV': D[L] = R
            case 'ADD': D[L] += R
            case 'CEQ': cmp = D[L] == R
            case 'CGE': cmp = D[L] >= R
            case DM if DM in ['MOD','DIV']:
                assert R != 0
                if DM == 'MOD':
                    D[L] %= R
                else:
                    D[L] //= R
    i += 1

assert len(res) in [1, 10]
assert res[0] in [ 1, 5, 111, 7745743850156157 ]

