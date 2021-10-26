def decompress(data, func = len, dec = 0):
    i = 0
    while i in range(len(data)):
        if data[i] == '(':
            j = data[i:].index(')')+1
            length, times = [int(x) for x in data[i:i+j][1:-1].split('x')]
            dec += func(*[x for x in [data[i+j:i+j+length], func] if x != len]) * times
            i = i + j + length
            continue
        else:
            dec += 1
        i+=1
    return dec


with open("C:\\Advent\\2016\\day9.txt", 'r') as file:
    data = file.read()
    dec = decompress(data)
    print(dec)
    dec = decompress(data, func = decompress)
    print(dec)
