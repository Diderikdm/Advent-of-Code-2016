with open("C:\\Advent\\2016\\day1.txt", 'r') as file:
    data = [x.split(', ') for x in file.read().splitlines()][0]
    calc = [lambda x,y,z : [(x,y+a) for a in range(1,z+1)], lambda x,y,z : [(x+a, y) for a in range(1,z+1)], lambda x,y,z : [(x, y-a) for a in range(1,z+1)], lambda x,y,z : [(x-a, y) for a in range(1,z+1)]]
    loc = (0,0)
    pts = [loc]
    p2 = None
    index = 0
    for instr in data:
        index = (index + 1 if instr.startswith('R') else index - 1)%4
        points = calc[index](loc[0], loc[1], int(instr[1:]))
        p2 = p2 or next(iter(x for x in points if x in pts and not p2), None)
        pts += points 
        loc = points[-1]

    print(abs(loc[0])+abs(loc[1]))
    print(abs(p2[0])+abs(p2[1]))
