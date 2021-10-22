with open("C:\\Advent\\2016\\day2.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    pad = [[1,2,3],[4,5,6],[7,8,9]]
    num = (1,1)
    move = {'U' : lambda x,y,z : max((x,z*0),(x,y-1)),
            'R' : lambda x,y,z : min((z,y),(x+1,y)),
            'D' : lambda x,y,z : min((x,z),(x,y+1)),
            'L' : lambda x,y,z : max((z*0,y),(x-1,y))}
    code = ''
    for n in data:
        for x in n:
            num = move[x](num[0], num[1], 2)
        code += str(pad[num[1]][num[0]])
    print(code)

    num = (0,2)
    pad2 = [[None,None,1,None,None],[None,2,3,4,None],[5,6,7,8,9],[None,'A','B','C',None],[None,None,'D',None,None]]
    move2 = {'U' : lambda x,y,z : move['U'](x,y,z) if pad2[max(y-1,z*0)][x] else (x,y),
             'R' : lambda x,y,z : move['R'](x,y,z) if pad2[y][min(x+1,z)] else (x,y),
             'D' : lambda x,y,z : move['D'](x,y,z) if pad2[min(y+1,z)][x] else (x,y),
             'L' : lambda x,y,z : move['L'](x,y,z) if pad2[y][max(x-1,z*0)] else (x,y)}
    code = ''
    for n in data:
        for x in n:
            num = move2[x](num[0], num[1], 4)
        code += str(pad2[num[1]][num[0]])
    print(code)
    
    
 
