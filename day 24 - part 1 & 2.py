from itertools import combinations
import sys
x=1500
sys.setrecursionlimit(x)

adj = lambda x,y : list(set([(x+a,y+b) for a,b in list(combinations([-1,0,1]*2, 2)) if sum([a,b]) in [-1,1] and len(grid[0]) > x+a >= 0 and len(grid) > y+b >= 0 and data[(x+a, y+b)] != '#']))

def find_matches(lst, total, override = False):
    trials = [k for k in result.keys() if k not in lst]
    for k in trials:
        find_matches(lst + [k], total + result[lst[-1]][k], override)
    if not trials:
        if override:
            all_matches[tuple(lst + [lst[0]])] =  total + result[lst[-1]][lst[0]]
        else:
            all_matches[tuple(lst)] = total


def find_route(current, steps = 0, path = [], bests = {}):
    bests[current] = steps
    for coord in [x for x in adj(*current) if x not in path]:
        if coord not in bests or bests[coord] > steps+1:
            if not(coord in bests and bests[coord] <= steps):
                find_route(coord, steps+1, path + [coord], bests)
    return bests


with open("C:\\Advent\\2016\\day24.txt", 'r') as file:
    grid = [[x for x in y] for y in file.read().splitlines()]
    data = {a[0] : a[1] for a in sum([[((x,y), z) for x,z in enumerate(row)] for y,row in enumerate(grid)], [])}
    nodes = [k for k,v in data.items() if v.isdigit()]
    result = {}
    for e,k in enumerate(nodes):
        result[k] = {x : y for x,y in find_route(k, 0, [], {}).items() if x in nodes}
    
    k = next(iter(k for k in nodes if data[k] == '0'), None)
    all_matches = {}
    find_matches([k], 0)
    print(min(all_matches.values()))
    all_matches = {}
    find_matches([k], 0, True)
    print(min(all_matches.values()))
