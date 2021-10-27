from itertools import combinations

def check_set(tup):
    chip = next(iter(x for x in tup if x in chips), None)
    if chip:
        gen = next(iter(x for x in tup if x in gens), None)
        if gen and sets[chip] != gen:
            return False
    return True

def check_current(trial):
    c = [x for x in trial if x in chips]
    if not c or c == trial:
        return True
    if any(not sets[x] in trial for x in c):
        return False
    return True

def trials(data, prev, i = 0, steps = 0):
    if (bests and 0 < steps > min(bests)):
        return
    elif next(iter(x for x in data if x), None) == data[3]:
        bests.append(steps)
    for idx in [i+1, i-1]:
        if 0 <= idx <= 3:
            dat = [tuple([x]) for x in data[i]] + [x for x in combinations(data[i], 2)] if idx < i else [x for x in combinations(data[i], 2)] + [tuple([x]) for x in data[i]]
            for x in filter(lambda x : len(x) == 1 or check_set(x), dat):
                temp = [y[:] for y in data]
                for z in x:
                    temp[idx].append(z)
                    temp[i].remove(z)
                if not check_current(temp):
                    continue
                t_new = tuple([(len([z for z in a if z in chips]), len([z for z in a if z in gens])) for a in temp] + [idx])
                if t_new not in prev and (not t_new in prevs or prevs[t_new] <= steps):
                    prevs[t_new] = steps+1
                    trials(temp, prev + [t_new], idx, steps+1)      


with open("C:\\Advent\\2016\\day11.txt", 'r') as file:
    from datetime import datetime
    e = datetime.now()
    data = [[z.strip('and ').strip(',') for z in y if not 'relevant' in z] for y in [x.strip('.').split('contains ')[1].split(', ') for x in file.read().replace(' and ', ', ').splitlines()]]
    floors = {e : x for e, x in enumerate(data)}
    bests = []
    prevs = {}
    chips = [x for x in sum(data,[]) if x.endswith('chip')]
    gens = [x for x in sum(data,[]) if x.endswith('generator')]
    sets = {k : next(iter(x for x in gens if x.startswith(k.split('-')[0])), None) for k in chips}
    trials([x[:] for x in data], [floors])
    print(min(bests))
    
    data[0] += ["elerium generator", "elerium-compatible microchip", "dilithium generator", "dilithium-compatible microchip"]
    bests = []
    prevs = {}
    chips = [x for x in sum(data,[]) if x.endswith('chip')]
    gens = [x for x in sum(data,[]) if x.endswith('generator')]
    sets = {k : next(iter(x for x in gens if x.startswith(k.split('-')[0])), None) for k in chips}
    trials([x[:] for x in data], [floors])
    print(min(bests))
