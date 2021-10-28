with open("C:\\Advent\\2016\\day18.txt", 'r') as file:
    data = [[1 if y == '.' else 0 for y in file.read()]]
    find = lambda x, lst : 0 if (lst[x-1] if x-1 >= 0 else 1) != (lst[x+1] if x+1 < len(lst) else 1) else 1
    for x in range(1, 40):
        data.append([find(y, data[x-1]) for y in range(len(data[0]))])
    print(sum(sum(data, [])))
    data = [data[0]]
    for x in range(1, 400000):
        data.append([find(y, data[x-1]) for y in range(len(data[0]))])
    print(sum(sum(x) for x in data))
