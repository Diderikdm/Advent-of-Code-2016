from itertools import combinations

def find_route(current, goal, steps = 0, path = []):
    bests[current] = steps
    for coord in [x for x in sorted(adj(*current), key = lambda x : absol(x, goal)) if x not in path]:
        if coord not in bests or bests[coord] > steps+1:
            if not(coord in bests and bests[coord] <= steps):
                find_route(coord, goal, steps+1, path + [coord])


with open("C:\\Advent\\2016\\day22.txt", 'r') as file:
    data = {[(int(b[1:]),int(c[1:])) for b,c in [a.split('-')[1:]]][0] : {'Size' : int(b), 'Used' : int(c), 'Avail': int(d), 'Use' : int(e)} for a,b,c,d,e in [[y.strip('T').strip('%') for y in x.split() if y] for x in [z.split('/')[-1] for z in file.read().splitlines()[2:]]]}
    matches = set()
    for k,v in data.items():
        for k2, v2 in data.items():
            if k != k2 and 0 < v['Used'] <= v2['Avail']:
                matches.add((k,k2))
    print(len(matches))
    grid = [['_' if data[(x,y)]['Use'] < 10 else ('#' if data[(x,y)]['Use'] > 85 else '.') for x in range(sorted(data)[-1][0] + 1)] for y in range(sorted(data, key = lambda z: z[1])[-1][1] + 1)]
    start = next(iter(k for k,v in data.items() if v['Use'] < 10), None)
    goal = (len(grid[0])-1, 0)
    adj = lambda x,y : list(set([(x+a,y+b) for a,b in list(combinations([-1,0,1]*2, 2)) if sum([a,b]) in [-1,1] and len(grid[0]) > x+a >= 0 and len(grid) > y+b >= 0 and data[(x+a, y+b)]['Use'] <= 85]))
    absol = lambda x,y : sum([abs(x[1]-y[1]), abs(x[0]-y[0])])
    bests = {}
    find_route(start, goal)
    print(bests[goal] + 5 * (len(grid[0])-2))
