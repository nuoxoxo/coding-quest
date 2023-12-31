D = {}
for line in open(0).read().splitlines():
    _, qty, key = line.split()
    D[key] = D[key] + int(qty) if key in D else int(qty)
res = 1
for n in D.values():
    res *= n % 100
print('res/',res)
assert res in [ 13327755200, 187733700 ]
