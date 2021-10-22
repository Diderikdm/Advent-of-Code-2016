with open("C:\\Advent\\2016\\day3.txt", 'r') as file:
    data = [[int(y) for y in x.split(' ') if y] for x in file.read().splitlines()]
    print(len([x for x in data if max(x) < sum(sorted(x)[:2])]))
    print(len([a for a in sum([[[x[y] for x in data[z:z+3]] for z in range(0, len(data)-1, 3)] for y in range(3)],[]) if max(a) < sum(sorted(a)[:2])]))
