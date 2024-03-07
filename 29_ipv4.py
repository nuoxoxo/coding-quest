lines = open('29.0').read().splitlines()

def brute_force(lines) -> None:
    print('/bruteforce')
    Is = '192.168.0.0'
    Ie = '192.168.254.254'
    Ps = '10.0.0.0'
    Pe = '10.0.254.254'
    IN, OUT = 0, 0
    def inside(line, s, e):
        s, e = [int(_) for _ in s.split('.')], [int(_) for _ in e.split('.')]
        for i in range(4):
            if not s[i] <= line[i] <= e[i]:
                return False
        return True
    EXT = []
    for line in lines:
        temp = line[24:32]
        S = []
        for i in range(0,7,2):
            S.append(int( temp[i:i+2],16 ))
        temp = line[32:41]
        D = []
        for i in range(0,7,2):
            D.append(int( temp[i:i+2],16 ))
        N = int(line[4:8], 16)
        if inside(S, Is, Ie) or inside(D, Is, Ie):
            IN += N
        elif inside(S, Ps, Pe) or inside(D, Ps, Pe):
            OUT += N
        else:EXT.append([S, D])
    print('/ext', len(EXT))
    if len(EXT) != 0:
        print('/top', EXT[0])
    print('/res', str(IN) + '/' + str(OUT))

[ brute_force ][ 0 ]( lines )
