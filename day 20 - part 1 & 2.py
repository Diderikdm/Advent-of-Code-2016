with open("C:\\Advent\\2016\\day20.txt", 'r') as file:
    data = sorted([[int(x) for x in y.split('-')] for y in file.read().splitlines()], key = lambda z : z[0])
    first, nbl, mx = None, 0, 0
    for e, x in enumerate(data[:-1]):
        mn, mx = x if mx < x[1] else (x[0], mx)
        if mx + 1 < data[e+1][0]:
            first = first or mx + 1
            nbl += (data[e+1][0] - (mx+1))

    print(first)
    print(nbl + (4294967295 - max(x[1] for x in data)))
