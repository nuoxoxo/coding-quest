lines='''keyless YYBBYYG
society YGYYYBB
phobias BBGBGBG'''

words = open (0).read().splitlines()
from collections import defaultdict
badpos=defaultdict(list)
without=set()
goodpos={}

for line in lines.split('\n'):
    L, R = [list(_)for _ in line.split(' ')]
    idx = 0
    for l, r in zip(L, R):
        if r == 'B':
            without.add(l)
        if r == 'Y':
            badpos[idx].append(l)
        if r == 'G':
            goodpos[idx] = l
        idx += 1

print('idx2c:',goodpos)
for _ in badpos.items():print('badpos:',_)

guess = set()
for word in words:
    if all([ word[i] == c for i, c in goodpos.items()]):
        guess.add( word )
    if not all([ char in word for arr in badpos.values() for char in arr ]):
        guess.discard( word )
    if any([ word[i] in arr for i, arr in badpos.items()]):
        guess.discard( word )
    if any([ char in word for char in without ]):
        guess.discard( word )
for word in guess:print(word)
