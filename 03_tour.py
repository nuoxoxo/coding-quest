import math
coors = [list(map(int, line.split(' '))) for line in open (0).read().splitlines()]
res = 0
for i in range(1, len(coors)):
    x, y, z = coors[i]
    a, b, c = coors[i - 1]
    x = abs(x - a)
    y = abs(y - b)
    z = abs(z - c)
    res += math.floor( math.sqrt(x*x + y*y + z*z) )
print(res)
assert (res==64579603)
