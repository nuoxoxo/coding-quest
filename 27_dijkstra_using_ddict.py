lines = [_.split(' => ') for _ in open(0).read().splitlines()]
from collections import defaultdict
import heapq

f,t,extra_cost=('TYC','EAR',600) if len(lines) > 100 else ('AAA','ZZZ',10)

G = defaultdict(dict) # graph representation : Dict of Dict
for start, R in lines:
    R = R.split()
    for r in R:
        target, dist = r.split(':')
        G[ start ][ target ] = int(dist)

def print_ddict( G ):
    for k,v in G.items():print(f'node/{k}/',v)

print_ddict( G )

def dijkstra( G, start, end, extra_cost ):
    Q = [ (0, start, []) ] # heapQ # is it possible
    seen = set()
    while Q:
        cost, node, path = heapq.heappop( Q )
        """
        # unnecessary and slow
        if (node, cost) in seen:
            continue
        seen.add( (node, cost) )
        """
        if node in seen:
            continue
        seen.add( node )
        path = path + [node]
        if node == end:
            return ( cost - extra_cost, path ) 
        for next_node, next_cost in G[node].items():
            new_cost = cost + next_cost + extra_cost
            heapq.heappush( Q, (new_cost, next_node, path))
    return ( 1e9, [] )

res, path = dijkstra ( G, f, t, extra_cost )

print('res/',res)
print('path/','->'.join( path ))

assert res in [ 115,165127 ]

