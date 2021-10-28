def calc(i=0):
    while any((i - (data[e][0] - data[e][1] - (e+1))) % data[e][0] != 0 for e,x in enumerate(data)):
        i+=1
    return i

with open("C:\\Advent\\2016\\day15.txt", 'r') as file:
    data = [[int(x.strip('.').split()[y]) for y in [3,-1]] for x in file.read().splitlines()]
    print(calc())
    data = data + [[11,0]]
    print(calc())
