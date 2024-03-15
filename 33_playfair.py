suffix = 0
key, cipher = [_.split(':')[1].strip() for _ in open('33.0').read().strip().split('\n\n')]
s1, s2 = open('33.0').read().strip().split('\n\n')
key = s1.split(':')[1].strip()
cipher = s2.split(':')[1].strip()

if suffix == 1:
    key = 'helloworld'
    cipher = 'wp nehslv ewgw'
print('/Key \t|', key)
print('/Cipher\t|', cipher)

S = [False] * 26
PF = []
a = ord('a')
for c in key:
    assert c.isalpha()
    assert c.islower()
    pos = ord(c) - a
    if not S[pos]:
        PF.append(c)
        S[pos] = True
for i, boo in enumerate(S):
    if not boo:
        c = chr(i + a)
        if c != 'j':
            PF.append( c )
            S[i] = True
   
print('/Playfair->str |', ''.join(PF))
G = []
edge = int(len(PF) ** .5)
for i in range(edge):
    temp = []
    for j in range(edge):
        temp.append( PF[i * 5 + j] )
    G.append(temp)

spaces = [i for i,c in enumerate(cipher) if c == ' ']
print('/spaces->index |', spaces)

charset = [_ for _ in cipher if _ != ' ']
print('/charset->str  |', ''.join(charset))

N = len(charset)
assert N % 2 == 0

res = charset.copy()

for i in range(0, N - 1, 2):
    def finder(c):
        for i in range(edge):
            for j in range(edge):
                if G[i][j] == c:
                    return (i, j)
        assert False
        return None
    a, b = charset[i], charset[i+1]
    r, c = finder(a) 
    rr, cc = finder(b)
    sub1, sub2 = None, None
    if r != rr and c != cc:
        sub1 = G[r][cc]
        sub2 = G[rr][c]
    elif r == rr:
        sub1 = G[r][-1] if c == 0 else G[r][c-1]
        sub2 = G[rr][-1] if cc == 0 else G[rr][cc-1]
    elif c == cc:
        sub1 = G[-1][c] if r == 0 else G[r-1][c]
        sub2 = G[-1][cc] if rr == 0 else G[rr-1][cc]
    else:assert False
    assert sub1
    assert sub2
    res[i] = sub1
    res[i+1] = sub2

# recover original spaces
for i in spaces: res = res[:i] + [' '] + res[i:]

res = ''.join(res)
size = len(res)
assert size in [42, 14]
print('/len', size)
print('/res', res)
