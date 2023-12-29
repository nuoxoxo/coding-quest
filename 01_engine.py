lines = list(map(int, open(0).read().splitlines()))

res,cur,end=0,0,60
while end < len(lines) + 1:
    res += not 1500 <= sum(lines[cur:end]) // 60 <= 1600
    cur += 1
    end += 1
print(res)
assert(res in [6248])
