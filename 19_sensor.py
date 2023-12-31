B = [int(_)for _ in open(0).read().splitlines()]
epar = []
"""
# original soln
for b in B:
    bins = format(bin(b))
    bins = bins[2:].zfill(16)
    ones = bins.count('1')
    if ones % 2 == 0:
        temp = list([*bins])
        print(b, temp, temp[-1])
        temp[0] = '0'
        newb = ''.join(temp)
        epar.append(int(newb, 2))
"""

epar = [(int('0' + format(b, '016b')[1:], 2)) for b in B if bin(b).count('1') % 2 == 0]
res = round(sum(epar) / len(epar))
print('res/',res)

assert res in [ 297, 17837 ]

print('par/',epar)
