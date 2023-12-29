line = open(0).read().strip()
binstr = '000'+bin(int(line, 16))[2:]

D = {}
with open('infile') as file:
    for line in file:
        val, key = line.strip().split(' ')
        D[key] = val

res=''
l = 0
while l < len(binstr) - 3:
    r = l + 4
    char = binstr[l:r]
    if char not in D:
        r += 1
        char = binstr[l:r]
    if char not in D:
        r += 2
        char = binstr[l:r]
    if char not in D:
        break
    res += D[char]
    l = r
print(res)

