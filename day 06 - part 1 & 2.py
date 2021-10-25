with open("C:\\Advent\\2016\\day6.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    ans, ans2 = '', ''
    for x in range(len(data[0])):
        column = [row[x] for row in data]
        column = sorted(column, key = lambda y: column.count(y))
        ans += column[-1]
        ans2 += column[0]

    print(ans)
    print(ans2)
