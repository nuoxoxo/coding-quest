lines = [[ int(_) for _ in line.split()] for line in open(0).read().splitlines()]
start = -1
for i in range(len(lines)):
    if len(lines[i]) == 2:
        start = i
        break

moves = lines[start:] # get moving sequence
grid = lines[:start][::-1]
path = [] # get a flattened board
for i in range(len(grid)):
    path += grid[i][::-1] if i % 2 == 1 else grid[i]

assert len(moves) in [20, 500]
assert len(path) % 2 == 0

p1, p2 = 0, 0
res = None
for i, move in enumerate( moves ):
    d1, d2 = move
    def play(p, d): # player, dice
        p += d
        if p >= len(path) - 1: return ( True, p )
        while path[ p ] != 0:
            p += path[p]
            if p >= len(path) - 1: return ( True, p )
        return ( False, p )
    win, p1 = play( p1, d1 )
    if win:
        res = i+1
        print('win/',res)
        break
    win, p2 = play( p2, d2)
    if win:
        res = (i+1)*2
        print('win/',res)
        break

print(res)
assert res in [95, 13]

"""
# original #
for i, move in enumerate( moves ):
    d1, d2 = move
    p1 += d1
    if p1 >= len(path) - 1:
        print('win 1/',i+1)
        break
    while path[ p1 ] != 0:
        p1 += path[p1]
        if p1 >= len(path) - 1:
            print('win/',i+1)
            exit (0)
    p2 += d2
    if p2 >= len(path) - 1:
        print('win 2/',(i+1)*2)
        break
    while path[ p2 ] != 0:
        p2 += path[p2]
        if p2 >= len(path) - 1:
            print('win 2/',(i+1)*2)
            exit (0)
"""

