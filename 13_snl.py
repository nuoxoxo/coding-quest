lines = [[ int(_) for _ in line.split()] for line in open(0).read().splitlines()]
start = -1
for i in range(len(lines)):
    if len(lines[i]) == 2:
        start = i
        break
print(start)

moves = lines[start:] # get moving sequence
grid = lines[:start][::-1]
path = [] # get a flattened board
for i in range(len(grid)):
    path += grid[i][::-1] if i % 2 == 1 else grid[i]

print(path)
print(moves[0])
assert len(moves) in [20, 500]
assert len(path) % 2 == 0

p1, p2 = 0, 0
for i, move in enumerate( moves ):
    d1, d2 = move
    p1 += d1
    if p1 >= len(path) - 1:
        i+=1
        print('win 1/',i)
        break
    while path[ p1 ] != 0:
        p1 += path[p1]
        if p1 >= len(path) - 1:
            i+=1
            print('win/',i)
            exit (0)
    p2 += d2
    if p2 >= len(path) - 1:
        i += 1
        print('win 2/',i*2)
        break
    while path[ p2 ] != 0:
        p2 += path[p2]
        if p2 >= len(path) - 1:
            i += 1
            print('win 2/',i*2)
            exit (0)
# 95
