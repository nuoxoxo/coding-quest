lines = open('29.0').read().splitlines()
#lines = open('test').read().splitlines()

def brute_force(lines) -> None:
    print('/bruteforce')
    Is = '192.168.0.0'
    Ie = '192.168.254.254'
    Ps = '10.0.0.0'
    Pe = '10.0.254.254'
    IN, OUT = 0, 0
    def within(line, s, e):
        s = [int(_) for _ in s.split('.')]
        e = [int(_) for _ in e.split('.')]
        res = True
        line = [int(_) for _ in line.split('.')]
        for i in range(4):
            if not s[i] <= line[i] <= e[i]:
                res = False
                break
        return res
    EXT = set()
    for line in lines:
        temp = line[24:32]
        S = []
        for i in range(0,7,2):
            S.append(str(int( temp[i:i+2],16 )))
        S = '.'.join(S)
        temp = line[32:41]
        D = []
        for i in range(0,7,2):
            D.append(str(int( temp[i:i+2],16 )))
        D = '.'.join(D)
        N = int(line[4:8], 16)
        if within(S, Is, Ie) or within(D, Is, Ie):
            IN += N
        if within(S, Ps, Pe) or within(D, Ps, Pe):
            OUT += N
        else:EXT.add((S, D))
    print('/ext', len(EXT))
    print('/res', str(IN) + '/' + str(OUT))

[ brute_force ][ 0 ]( lines )
