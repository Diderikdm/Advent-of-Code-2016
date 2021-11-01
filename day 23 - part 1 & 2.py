with open("C:\\Advent\\2016\\day23.txt", 'r') as file:
    dat = [x.split() for x in file.read().splitlines()]
    for x in [7, 12]:
        data = [y[:] for y in dat]
        registers = {'a' : x, 'b' : 0, 'c' : x, 'd' : 0}
        i = 0
        while i in range(len(data)):
            try:
                if data[i][0] == 'cpy':
                    registers[data[i][2]] = registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1]) if data[i][2] in registers else 1/0
                elif data[i][0] == 'inc':
                    registers[data[i][1]] += 1
                elif data[i][0] == 'dec':
                    registers[data[i][1]] -= 1
                elif data[i][0] == 'jnz' and (registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1])) != 0:
                    i += registers[data[i][2]] if not data[i][2].strip('-').isdigit() else int(data[i][2])
                    continue
                elif data[i][0] == 'tgl':
                    target = i + registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1])
                    if target in range(len(data)):
                        if len(data[target]) == 2:
                            data[target][0] = 'dec' if data[target][0] == 'inc' else 'inc'
                        else:
                            data[target][0] = 'cpy' if data[target][0] == 'jnz' else 'jnz'
            except:
                i+=1
                continue
            i+=1
        print(registers['a'])
