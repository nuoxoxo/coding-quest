lines = open(0).read().splitlines()

fruits = [tuple(map(int,coor.split(','))) for coor in lines[1].split()]
steps = lines[-1]
D = {'L':[0,-1],'R':[0,1],'U':[-1,0],'D':[1,0]}
# print(fruits)
# print(steps)
# print(D)

def move(snake, R, C, F, step):

    dc, dr = D[step] # important:...
    r, c = snake[0] # i-n-v-e-r-s-e-d xD
    last = (r,c)
    r += dr
    c += dc
    # endgame on out of bound
    if not ( -1<r<R and -1<c<C ):
        return []#'END'
    # collides itself
    if (r,c) in snake:
        return []#'END'
    # append the head w/o moving the body on Fruit
    if F and (r,c) == F[::-1]:
        return ([(r,c)] + snake, True)
    # a bodybloc steps to its previous bodybloc
    snake[0] = (r,c)
    for i in range(1, len(snake)):
        temp = snake[i]
        snake[i] = last
        last = temp
    return ( snake, False )

def DBG(i,res,Snake, R, C, f):

    print(i,'DBG/res/',res,'snk/',Snake,'f/',f[::-1])
    G = [['.' for _ in range(R)] for _ in range(R)]
    r,c = f
    G[r][c]='F'
    for r,c in Snake: G[c][r] = 'S'
    for line in G: print(''.join(line))

def game(fruits, steps, D):

    res = 0
    Snake = [(0,0)]
    R = C = 8 if len(fruits) == 4 else 20
    f = tuple(fruits.pop(0))[::-1] if fruits else []
    for i, step in enumerate(steps):
        state = move(Snake, R, C, f, step)
        if not state:
            print('steps/',i + 1,'res/',res)
            break
        Snake, Eat = state
        if Eat:
            res += 100
            if f: f = tuple(fruits.pop(0))[::-1] if fruits else []
        if i in [49,50,99,100]:DBG(i+1, res, Snake, R, C, f) # long input dbg
        if len(fruits) < 10: DBG(i + 1, res, Snake, R, C, f) # Sample dbg
        res += 1
    return res

res = game (fruits, steps, D)
print( res )

assert res in [320, 4240]
