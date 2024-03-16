from collections import deque

def Solver(G):
    DR, DC = [0,-1,0,1], [-1,0,1,0]
    levels = len(G)
    assert levels == 2
    R, C = len(G[0]), len(G[0][0])
    start, end = (0, 1, 0), (0, R - 2, C - 1)
    Q = deque()
    Q.append((start, 1))

    Seen = set()
    Seen.add(start)
    path = {}
    while Q:
        pos, res = Q.popleft()
        L, r, c = pos
        if pos == end:
            fullpath = [end]
            while pos != start:
                pos = path[pos]
                fullpath.append(pos)
            fullpath = fullpath[::-1]
            return res, fullpath

        for dr, dc in zip(DR, DC):
            rr, cc = r + dr, c + dc
            if not -1 < rr < R or not -1 < cc < C or G[L][rr][cc] == '#':
                continue
            if (L, rr, cc) not in Seen:
                Seen.add((L, rr, cc))
                Q.append(((L, rr, cc), res + 1))
                path[(L, rr, cc)] = pos
            if G[L][rr][cc] == '$' and (1 - L, rr, cc) not in Seen:
                Seen.add((1 - L, rr, cc))
                Q.append(((1 - L, rr, cc), res + 1))
                path[(1 - L, rr, cc)] = pos
    return -1, []

RES = []

for i in [0,1]:
  G = [[[c for c in s] for s in _.splitlines()] for _ in open('36.' + str(i)).read().split('\n\n')]
  res, fullpath = Solver(G)

  for lv, r, c in fullpath:G[lv][r][c] = '@'

  for r in range(len(G[0])):
    for c in range(len(G[0][r])):
      if G[0][r][c] == '.': G[0][r][c] = ' '
      if G[0][r][c] == '#': G[0][r][c] = '-'
      if G[0][r][c] == '$': G[0][r][c] = 'x'
  for r in range(len(G[1])):
    for c in range(len(G[1][r])):
      if G[1][r][c] == '.': G[1][r][c] = ' '
      if G[1][r][c] == '#': G[1][r][c] = '-'
      if G[1][r][c] == '$': G[1][r][c] = 'x'

  for g in G:
    for gg in g:print(''.join(gg))
    print()
  print('/path 👆')
  print('/res', res)
  print('/maze', i, '/end \n')
  RES.append(res)

assert all([_ in [53, 251] for _ in RES])
