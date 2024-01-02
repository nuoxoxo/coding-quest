# Traveling Salesman Problem
# in a stripped down form be like:

def backtracking_dfs (curr, G, remain, states):
    ### curr :
    # current shop
    # current r,c position in the permutation of visited shops
    if not remain:
    ### remain:
    # a set of remaining 'un'visited shops
    # a set of all shops except the 1st shop at 0,0 and the current shop
        print('curr/',curr)
        print('G[curr]/',G[curr])
        print('G[curr][0]/',G[curr][0],'\n')
        return G[ curr ][0]
        # if we reach the end, we have a result for comparing in Backtracking
        # this path/distance is not always the most efficient/shortest
    state = ( curr, tuple(remain) )
    if state in states:
        # this steps makes it faster
        return states[ state ]
    # if this state is computed before and stored, return it

    min_dist = 1e9
    for shop in remain:
        update_remain = remain - {shop}
        # Backtrack
        dist = G[ curr ][ shop ] + backtracking_dfs (shop, G, update_remain, states)
        min_dist = min(min_dist, dist)
    states[ (curr,tuple(remain)) ] = min_dist
    return min_dist

G = [[int(_) for _ in line.split(' ')] for line in open(0).read().splitlines()]
N = len(G)

res = backtracking_dfs (
    0,
    G,
    set( range(1, N) ), # n-2 number of remaining shops to visit
    dict(), 
)

print('res/',res)
