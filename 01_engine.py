lines = list(map(int, open(0).read().splitlines()))

res,cur,end=0,0,60
while end < len(lines) + 1:
    res += 1 if not (1500 <= sum(lines[cur:end]) // 60 <= 1600) else 0
    cur += 1
    end += 1
print(res)
