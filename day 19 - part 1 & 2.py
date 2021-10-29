from math import log, floor

data = 3017957
linked = {x : x+1 for x in range(1, data)}
linked[data] = 1
current = 1
while len(linked) > 1:
    elim = linked[current]
    linked[current] = linked[linked[current]]
    linked.pop(elim)
    current = linked[current]

print(current)

def calc(data):
    x = floor(log(data, 3))
    y = data - 3**x
    return data if y == 0 else (y if x == 1 or y <= (3**x) else 3**x + 2 * (y-3**l))

print(calc(data))
