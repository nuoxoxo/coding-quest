# tic-tac-toe bruteforced

def play(T, p):
    t = list(dict(sorted(T.items())).values())
    # 3 rows
    t = [ t[0:3], t[3:6], t[6:9] ]
    if all(n == p for n in t[0]) \
    or all(n == p for n in t[1]) \
    or all(n == p for n in t[2]):
        return ( True, p )
    # 3 cols
    if all(n == p for n in list(zip(*t))[0]) \
    or all(n == p for n in list(zip(*t))[1]) \
    or all(n == p for n in list(zip(*t))[2]):
        return ( True, p )
    # diagonal x2
    t = [n for row in t for n in row]
    if all(n == p for n in [ t[0],t[4],t[8] ]) \
    or all(n == p for n in [ t[2],t[4],t[6] ]):
        return ( True, p )
    # draw|unfinished if all win-conds skipped
    return ( True, 'Draw' ) if all(n != 0 for n in t) else ( False, 'Unfinished' )

end = [0, 0, 0] 
for line in [[int(_) for _ in line.split()] for line in open(0).read().splitlines()]:
    T = {}
    for i in range(1,10): T[i] = 0
    for i, n in enumerate(line):
        p = i % 2 + 1
        T[n] = p
        endgame, verdict = play(T, p)
        if endgame:
            if verdict == 'Draw':
                end[2] += 1
            else:
                end[ verdict-1 ] += 1
            break

res = 1
for n in end:
    res *= n
print('res/', res)
print('end/', end)

assert res in [ 20938290, 0 ]

