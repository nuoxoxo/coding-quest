SIDE, WIN = 7, 4
games = open(0).read().splitlines()

def checkgame(G): # return a tuple: ( bool, None|int(who_wins), str )
    assert len(G)==len(G[0])==SIDE
    # check rows in R-growing list ie. vertical in real board
    for row in G:
        tt=1
        who=None
        for i in range(len(row) - 1):
            if row [i] == None:
                continue
            if row[i] == row[i + 1]:
                tt += 1
                who = row[i]
                if tt >= WIN:
                    return ( True, who, 'Vertical' )
            else:
                tt = 1
                who = None
    # check cols in R-growing list: ground-up horizontal in real board
    for col in zip(*G):
        tt=1
        who=None
        for i in range(len(col) - 1):
            if col [i] == None:
                continue
            if col[i] == col[i + 1]:
                tt += 1
                who = col[i]
                if tt >= WIN:
                    return ( True, who, 'Horizontal' )
            else:
                tt = 1
                who = None
    # check diagonal wins 1/2 : '\'
    for r in range(WIN):
        for c in range(WIN):
            tt=1
            who=None
            i = -1
            while True:
                i += 1
                if SIDE in [r+i, c+i, r+i+1, c+i+1]:
                    break
                if G[r+i][c+i] == None:
                    continue
                if G[r+i][c+i] == G[r + i + 1][c + i + 1]:
                    tt += 1
                    who = G[r+i][c+i]
                    if tt >= WIN:
                        return ( True, who, 'Diagonal' )
                else:
                    tt = 1
                    who = None
    # check diagonal wins 2/2 : '/'
    for r in range(3,3+WIN):
        for c in range(WIN):
            tt=1
            who=None
            i = -1
            while True:
                i += 1
                if SIDE in [c+i, c+i+1] or -1 in [r-i,r-i-1]:
                    break
                if G[r-i][c+i] == None:
                    continue
                if G[r-i][c+i] == G[r - i - 1][c + i + 1]:
                    tt += 1
                    who = G[r-i][c+i]
                    if tt >= WIN:
                        return ( True, who, 'Diagonal' )
                else:
                    tt = 1
                    who = None
    if sum([row.count(None) for row in G]) == 0:
        return (True, 'Draw', '0 slot available')
    return (False, -1, 'unfinished') 

"""
dbg=[\
    [1, 2, 3, 3, None, None, None],\
    [2, 2, 3, 1, 2, 1, 1],\
    [2, 3, 1, 2, None, None, None],\
    [3, 1, 1, 1, None, None, None],\
    [3, 2, None, None, None, None, None],\
    [3, 1, 3, 3, None, None, None],\
    [2, 3, 1, 2, 2, 1, None]]
print(checkgame(dbg))

test=[ \
    [None, None, None, None, None, None, None],\
    [None, None, 4, None, None, None, None],\
    [None, None, 3, 4   , None, None, None],\
    [2,    None, 3, None, 4   , None, 1],\
    [None, 1   , 3, None, None, 1   , None],\
    [None, None, 1, None, 1   , None, None],\
    [None, None, None, 1, None, None, None]]
print(checkgame(test))

exit()
"""

winners={}
for game in games:
    G = [[None for _ in range(SIDE)] for _ in range(SIDE)]
    rows=[int(_)-1 for _ in game] # R-growing, all moves 'dropped' to left
    player = 1
    res = None
    for n in rows:
        assert n < SIDE
        idx = 0
        while G[n][idx] != None:
            idx += 1
        assert idx < SIDE
        G[n][idx] = player
        res = checkgame(G)
        if res[0]:
            break
        player = player % 3 + 1

    assert isinstance(res, tuple)
    assert len(res) == 3 
    if res[0]:
        who = res[1]
        if who not in winners:
            winners[ who ] = 1
        else:
            winners[ who ] += 1
    #for g in G:print(g)
    print(res)

assert sum(winners.values()) == len(games)

res = 1
for k, v in winners.items():
    print('player:',k,v)
    res *= v if isinstance(k, int) else 1
print(res)

assert res in [21630678]

