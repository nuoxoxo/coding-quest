lines = [list(map(int, line.split())) for line in open (0).read().splitlines()]
D = {3:1,4:10,5:100,6:1000}
W = list(map(int, '12 48 30 95 15 55 97'.split(' ')))

res = 0
for line in lines:
    wins = 0
    for n in line:
        if n in W:
            wins += 1
    if wins not in D:
        assert (wins < max(D.keys()))
    res += D[wins] if wins in D else 0

print('res/',res)
assert res in [110, 56]
