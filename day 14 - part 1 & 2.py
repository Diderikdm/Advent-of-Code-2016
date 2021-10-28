from hashlib import md5

def calc(times, triplets, quintlets, valids, i):
    while len(valids) < 64:
        trial = md5((data + str(i)).encode()).hexdigest()
        for x in range(times):
            trial = md5(trial.encode()).hexdigest()
        trip = next(iter(trial[x] for x in range(len(trial)-2) if len(set(trial[x:x+3])) == 1), None)
        if trip:
            triplets[i] = trip
        quint = next(iter(trial[x] for x in range(len(trial)-4) if len(set(trial[x:x+5])) == 1), None)
        if quint:
            quintlets[i] = quint
        if i-1001 in triplets:
            quints = [v for k,v in quintlets.items() if k in range(i-1000, i+1)]
            if triplets[i-1001] in quints:
                valids.append(i-1001)
            triplets.pop(i-1001)
        i+=1
    return valids[-1]

data = 'cuanljph'
print(calc(0, {}, {}, [], 0))
print(calc(2016, {}, {}, [], 0))
