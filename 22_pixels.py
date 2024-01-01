lines = [[ int(_) for _ in line.split(' ') ] for line in open(0).read().splitlines()]

#R = C = 8
R,C=10,50
G = [['.' for _ in range(C)] for _ in range(R)]

def printer(G) -> None:
    for g in G:print(' '.join(g))
    print()

for line in lines:
    sc, sr, dc, dr = line
    print(line)
    for r in range(sr, sr+dr):
        for c in range(sc, sc+dc):
            G[r][c] = '#' if G[r][c] == '.' else '.'
    printer(G)

printer(G)
