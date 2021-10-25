def find_abba(lst):
    return any(any([x[i] != x[i+1] and x[i:i+2] == ''.join(x[i+3:i+1:-1]) for i in range(len(x)-3)]) for x in lst)

def find_aba(lst):
    return sum([[x[i:i+3] for i in range(len(x)-2) if x[i] != x[i+1] and x[i] == x[i+2]] for x in lst], [])

def find_bab(lst, hypernets):
    return any(any(y in x for y in [z[1]+z[0]+z[1] for z in lst]) for x in hypernets)

with open("C:\\Advent\\2016\\day7.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    result, r2 = [], []
    for ip in data:
        vals = ip.split('[')
        nets = [vals[0]]
        hypernets = []
        for x in vals[1:]:
            hypernet, net = x.split(']')
            nets.append(net)
            hypernets.append(hypernet)
        if find_abba(nets) and not find_abba(hypernets):
            result.append(ip)
        if find_bab(find_aba(nets), hypernets):
            r2.append(ip)
            
    print(len(result))
    print(len(r2))
