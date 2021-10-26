with open("C:\\Advent\\2016\\day10.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
    last_bot = max(max(int(x) for x in row if x.isdigit()) for row in data)
    previous = []
    outputs = {e : [] for e in range(0, last_bot+1)}
    bots = {e : [] for e in range(0, last_bot+1)}
    start = [x for x in data if x[0] == 'value']
    gives = {int(x[1]) : {0 : [x[5], int(x[6])], 1 : [x[-2], int(x[-1])]} for x in data if x[0] == 'bot'}
    for x in start:
        bots[int(x[-1])].append(int(x[1]))
    while True:
        for x,y in filter(lambda x: x[0] not in previous and len(bots[x[0]]) == 2, gives.items()):
            previous.append(x)
            mn, mx = sorted(bots[x])
            if 'bot' in y[0]:
                if mn not in bots[y[0][1]]:
                    bots[y[0][1]].append(mn)
            else:
                if mn not in outputs[y[0][1]]:
                    outputs[y[0][1]].append(mn)
            if 'bot' in y[1]:
                if mx not in bots[y[1][1]]:
                    bots[y[1][1]].append(mx)
            else:
                if mx not in outputs[y[1][1]]:
                    outputs[y[1][1]].append(mx)
            break
        else:
            break

    print(next(iter(k for k,v in bots.items() if 61 in v and 17 in v), None))
    print(outputs[0][0] * outputs[1][0] * outputs[2][0])
