IN = 2
DIR = [
    (0, -1), # U
    (1, -1), # UR
    (1, 0), # R
    (1, 1), # DR
    (0, 1), # D
    (-1, 1), # DL
    (-1, 0), # L
    (-1, -1), #UL
]
G = [_.split(' ') for _ in open('37.' + str(IN)).read().splitlines()]

side = 20
if IN == 1: side = 6
mid = side // 2
x,o = 'x','o'
tokens = [o,x]

def makeBoard(side):
    B = [['.'] * side for _ in range(side) ]
    B[mid-1][mid-1], B[mid][mid] = o,o
    B[mid-1][mid], B[mid][mid-1] = x,x
    return B

def printer(B):
    for b in B: print(' '.join(b))
    print('/end board')

def parseMove(s:str): # return a (r,c) tuple
    return ( ord(s[0])-ord('a'), int(s[1:])-1  )

def isMoveValid(B,player,move):
    r, c = parseMove(move)
    if not -1 < r < side or not -1 < c < side or B[r][c] != '.':
        return False
    for dr,dc in DIR:
        ofs = 1
        while -1 < r + dr * ofs < side and -1 < c + dc * ofs < side and \
            B[r + dr * ofs][c + dc * ofs] == tokens[1-player]:
                ofs += 1
        if -1 < r + dr * ofs < side and -1 < c + dc * ofs < side and \
            B[r + dr * ofs][c + dc * ofs] == tokens[player]: # found a remote one that is my token
                return True
    #printer(B)
    print('/👆invalid move',move, '/player', tokens[player], '/pos',r, c)
    return False

def countTokens(B,player):
    res = 0
    for r in B:
        for c in r:
            if c == tokens[player]:
                res += 1
    return res

p1,p2 = 0,0

for moves in G:
    B = makeBoard(side)
    for i, move in enumerate(moves):
        player = i % 2
        #print('/player', player, move, parseMove(move)) # Player 1 is Even-indexed
        r, c = parseMove( move )
        if not isMoveValid(B, player, move):
            break
        B[r][c] = tokens[player]
        for dr,dc in DIR:
            ofs = 1 # checking if a remote conn exists
            while -1 < r + dr * ofs < side and -1 < c + dc * ofs < side and \
                B[r + dr * ofs][c + dc * ofs] == tokens[1-player]:
                ofs += 1
            endr, endc = r + dr * ofs, c + dc * ofs
            if not -1 < endr < side or not -1 < endc < side or \
                B[endr][endc] != tokens[player]: # found a remote one that is my token
                endr = None
                endc = None
            """if move == 'b2':
                print('/bug', endr, endc)"""
            ofs = 1 # reset to execute a valid attack
            if endr != None and endc != None:
                while -1 < r + dr * ofs < side and -1 < c + dc * ofs < side and \
                    B[r + dr * ofs][c + dc * ofs] == tokens[1-player]:
                    B[r + dr * ofs][c + dc * ofs] = tokens[player] # placing my token
                    ofs += 1
        if move in ['i15', 'l14']:
            printer(B)
            print(move)
        printer(B) # DBG
    print('/ended',player, r, c)
    printer(B) # DBG
    p1 += countTokens(B,0)
    p2 += countTokens(B,1)

print('/res',p1,p2)
