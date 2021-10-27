from itertools import combinations

adj = lambda x,y : list(set([(x+a,y+b) for a,b in list(combinations([-1,0,1]*2, 2)) if sum([a,b]) in [-1,1] and x+a >= 0 and y+b >= 0]))
absol = lambda x,y : sum([abs(x[1]-y[1]), abs(x[0]-y[0])])
calc = lambda x,y : 1 if (bin((x*x + 3*x + 2*x*y + y + y*y) + data).count('1'))%2 == 0 else 0

def find_route(current, goal, steps = 0, path = []):
    bests[current] = steps
    for coord in [x for x in sorted(adj(*current), key = lambda x : absol(x, goal)) if x not in path]:
        if coord not in bests or bests[coord] > steps+1:
            if calc(*coord):
                if not(coord in bests and bests[coord] <= steps):
                    find_route(coord, goal, steps+1, path + [coord])

         
data = 1362
current = (1,1)
goal = (31,39)
bests = {}
find_route(current, goal, path=[current])
print(bests[goal])
print(len([k for k,v in bests.items() if v <= 50]))
