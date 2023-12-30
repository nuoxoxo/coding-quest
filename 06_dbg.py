lines = open(0).read().splitlines()

from collections import defaultdict
D = defaultdict(int)
cmp = False

res = None
i = 0
#for i, line in enumerate(lines):
while True:
    print('line:',i)
    line = lines[i]
    expr = line.split(' ')
    # print(expr[0], expr)
    CMD = expr[0]
    assert len (expr) in [1,2,3]
    if len(expr) == 1: break
    elif len(expr) == 2:
        R = expr[1]
        if CMD == 'OUT':
            R = int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]
            print(R)
            res = R
        elif CMD == 'JIF' and cmp:
            R = int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]
            #print(i, R, i+R, len(lines))
            i = (i+R) % len(lines)
            continue
        elif CMD == 'JMP':
            R = int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]
            #print(i, R, i+R, len(lines))
            i = (i+R) % len(lines)
            continue
    elif len(expr) == 3:
        # print(expr)
        L, R = expr[1:]
        assert isinstance(L, str)
        match CMD:
            case 'ADD':
                R = int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]
                # R = int(R) if R.isdigit() or R[1:].isdigit() else D[R]
                D[L] += R
            case DM if DM in ['MOD','DIV']:
                R = int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]
                # R = int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]
                assert R != 0
                if DM == 'MOD':
                    D[L] %= R
                else:
                    D[L] //= R
            case 'MOV':
                R = int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]
                # R = int(R) if R.lstrip('-1').isdigit() else D[R]
                D[L] = R
            case 'CEQ':
                R = int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]
                assert i < len(lines) and lines[i+1].startswith('JIF')
                # R = int(R) if R.lstrip('-1').isdigit() else D[R]
                cmp = D[L] == R
            case 'CGE':
                assert i < len(lines) and lines[i+1].startswith('JIF')
                R = int(R) if R.isdigit() or len(R)>1 and R[1:].isdigit() else D[R]
                # R = int(R) if R.lstrip('-1').isdigit() else D[R]
                cmp = D[L] >= R
    i += 1

assert res in [ 7745743850156157 ]
