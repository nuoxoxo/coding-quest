from collections import defaultdict

packs = open(0).read().splitlines()

Ship = defaultdict(list)
for p in packs:
    if not p.startswith('5555'):
        continue
    idx = 4+8
    ship_hex = p[ 4:idx ]
    ship = int( ship_hex, 16 )
    #print('ship/hex,no.',ship_hex, ship)

    idx += 2
    order_hex = p[ 4:idx ]
    order = int (order_hex, 16)

    idx += 2
    assert idx == 16

    checksum_hex = p[ 4:idx ]
    checksum = int( checksum_hex, 16 )

    msg = p[idx:]
    assert len(msg) == 192//4

    checksum2 = 0
    decoded = ''
    for i in range(0, len(msg), 2):
        char = int(msg[i:i+2], 16)
        checksum2 += char
        decoded += chr( char )
    if checksum % 256 != checksum2 % 256:
        continue

    Ship[ ship ].append(( order, decoded ))

assert len(Ship) == 1
res = ''.join([_[1] for _ in sorted(list(Ship.values())[0])])

print(res)
assert res[0] == 'T'
assert res[-1] == '.'

