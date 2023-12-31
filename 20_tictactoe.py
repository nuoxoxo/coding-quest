def play(T, p):
    t = list(dict(sorted(T.items())).values())
    t = [ t[0:3], t[3:6], t[6:9] ]
    if (any(n == 0 for n in t)):
        return ( False, 'Draw' )
    if (all(n > 0 and n == p for n in t[0])):
        return ( True, p )
    if (all(n > 0 and n == p for n in t[1])):
        return ( True, p )
    if (all(n > 0 and n == p for n in t[2])):
        return ( True, p )
    if (all(n > 0 and n == p for n in list(zip(*t))[0])):
        return ( True, p )
    if (all(n > 0 and n == p for n in list(zip(*t))[1])):
        return ( True, p )
    if (all(n > 0 and n == p for n in list(zip(*t))[2])):
        return ( True, p )
    t = [n for row in t for n in row]
    if (all(n > 0 and n == p for n in [ t[0],t[4],t[8] ])):
        return ( True, p )
    if (all(n > 0 and n == p for n in [ t[2],t[4],t[6] ])):
        return ( True, p )
    return ( False, 'Unfinished' )

res = [0, 0, 0] 
for line in [[int(_) for _ in line.split()] for line in open(0).read().splitlines()]:
    print(line)
    T = {}
    for i in range(1,10): T[i] = 0
    for i, n in enumerate(line):
        p = i % 2 + 1
        T[n] = p
        win, player = play(T, p)
        if win:
            res[i % 2] += 1
            break
        elif player == 'Draw':
            res[2] += 1
end = 1
for n in res:
    end *= n
print(end)

