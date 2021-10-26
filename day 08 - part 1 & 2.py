with open("C:\\Advent\\2016\\day8.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
    grid = [[' ' for x in range(50)] for y in range(6)]
    for row in data:
        if row[0] == 'rect':
            maxx,maxy = [int(x) for x in row[1].split('x')]
            for y in range(maxy):
                for x in range(maxx):
                    grid[y][x] = '#'
        else:
            index = int(row[2].split('=')[-1])
            amt = int(row[-1])
            if row[1] == 'row':
                grid[index] = grid[index][-amt:] + grid[index][:-amt]
            else:
                temp = [grid[y][index] for y in range(len(grid))]
                arr_temp = temp[-amt:] + temp[:-amt]
                for y in range(len(grid)):
                    grid[y][index] = arr_temp[y]

    print(sum(1 for x in sum(grid, []) if x == '#'))
    print('\n'.join([''.join([x for x in y]) for y in grid]))
