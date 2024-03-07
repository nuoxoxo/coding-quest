lines = open('31.0').read().splitlines()[1:]
A = []
for line in lines:
    l = line.split()
    name, _, a, b, c = ' '.join(l[:-4]), l[-4], l[-3], l[-2], l[-1]
    print(name, '\n', _,a,b,c)
    A.append( (name, float(a), float(b), float(c)) )
print()
END = []
N = len(A)
for i in range(N):

    L, a,b,c = A[i]
    for j in range(i+1, N):
        R, x,y,z = A[j]
        print(L, a,b,c)
        print(R, x,y,z)
        aa, bb, cc = a-x, b-y, c-z
        res = ( aa**2 + bb**2 + cc**2 ) ** .5
        END.append(res)
    print()
for e in sorted(END,reverse=True):
    print(e)
