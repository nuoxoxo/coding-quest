lines = [_.split('|') for _  in open(0).read().splitlines()]

import hashlib
test="""Original iPhone still in box|\
3595421|\
0000000000000000000000000000000000000000000000000000000000000000|\
00000078f97879b26be6baf2adb520b126f84ed10464ed4e9a77b8ed87e07468\
""".split('|')
L='|'.join(test[:3]).encode()
print(hashlib.sha256( L ).hexdigest() == test[-1], test[-1])

def DBG(i, rec):
    print(i+1)
    for f in rec:print(f)

found = False
for i, rec in enumerate(lines):
    DBG (i, rec)
    old = rec[-1]
    L = '|'.join( rec[:3] ).encode()
    H = hashlib.sha256( L ).hexdigest()
    if not found and H != old:
        print(f'record no.{i+1} is bad\n(old) {old} \n(now) {H}')
        found = True
    if found:# and i < len(lines) - 1:
        mining = -1
        while True:
            mining += 1
            lines[i][1] = str(mining)
            L = '|'.join( rec[:3] ).encode()
            H = hashlib.sha256( L ).hexdigest()
            if H.startswith('000000'):
                rec[-1] = H
                if i < len(lines) - 1:
                    lines[i + 1][2] = H
                break
        print(f'(new) {rec[-1]}')
    print ()

