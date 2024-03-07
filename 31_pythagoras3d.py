lines = open('31.0').read().splitlines()[1:]
A = []
SEP = '\n\t'
for line in lines:
    l = line.split()
    name, _, a, b, c = '_'.join(l[:-4]), l[-4], l[-3], l[-2], l[-1]
    print(name, SEP, _, a,b,c)
    A.append( (name, float(a), float(b), float(c)) )
print('/end \n')
END = []
N = len(A)
for i in range(N - 1):
    L, a,b,c = A[i]
    print('/compare', L, SEP,a,b,c)
    for j in range(i+1, N):
        R, x,y,z = A[j]
        print('/against', R, SEP, x,y,z)
        aa, bb, cc = a-x, b-y, c-z
        res = ( aa**2 + bb**2 + cc**2 ) ** .5
        END.append((res, L, R))
    print()
for e in sorted(END)[:5]:
    #print(e)
    print(' ... '.join([str(_) for _ in list(e)]))
