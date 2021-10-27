with open("C:\\Advent\\2016\\day12.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
    for x in range(2):
        registers = {'a' : 0, 'b' : 0, 'c' : x, 'd' : 0}
        i = 0
        while i in range(len(data)):
            if data[i][0] == 'cpy':
                registers[data[i][2]] = registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1])
            elif data[i][0] == 'inc':
                registers[data[i][1]] += 1
            elif data[i][0] == 'dec':
                registers[data[i][1]] -= 1
            elif data[i][0] == 'jnz' and (registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1])) != 0:
                i += registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
                continue
            i+=1
        print(registers['a'])
