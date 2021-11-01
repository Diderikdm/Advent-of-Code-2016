with open("C:\\Advent\\2016\\day25.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
    end = None
    z = 0
    while not end:
        outs = []
        registers = {'a' : z, 'b' : 0, 'c' : 0, 'd' : 0}
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
            elif data[i][0] == 'out':
                val = registers[data[i][1]] if not data[i][1].strip('-').isdigit() else int(data[i][1])
                if outs and val == outs[-1]:
                    break
                outs.append(val)
                if len(outs) == 256 and len(set(x for x in outs[0:len(outs):2])) == 1 and len(set(x for x in outs[1:len(outs):2])) == 1:
                    end = z
                    break
            i+=1
      
        z += 1
                                
    print(end)
