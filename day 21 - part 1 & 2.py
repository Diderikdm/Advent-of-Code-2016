def calc(data, pw, rev=False):
    for inst in data:
        if inst[0] == 'swap':
            if inst[1] == 'position':
                pw[int(inst[2])], pw[int(inst[-1])] = pw[int(inst[-1])], pw[int(inst[2])]
            else:
                a, b = pw.index(inst[-1]), pw.index(inst[2])
                pw[a], pw[b] = pw[b], pw[a]
        elif inst[0] == 'rotate':
            if inst[1] == 'based':
                if not rev:
                    rot = (1 + pw.index(inst[-1]) + (1 if pw.index(inst[-1]) >= 4 else 0)) % len(pw) * -1
                else:
                    for pw_copy in [[y for y in pw[x:]] + [y for y in pw[:x]] for x in range(len(pw))]:
                        rot = (1 + pw_copy.index(inst[-1]) + (1 if pw_copy.index(inst[-1]) >= 4 else 0)) % len(pw) * -1
                        if pw_copy[rot:] + pw_copy[:rot] == pw:
                            rot *= -1
                            break
            else:
                rot = (int(inst[2])) % len(pw) * (-1 if inst[1] == ('left' if rev else 'right') else 1)
            pw = pw[rot:] + pw[:rot]
        elif inst[0] == 'reverse':
            x,y = int(inst[2]), int(inst[-1])
            pw = pw[:x] + pw[x:y+1][::-1] + pw[y+1:]
        else:
            m = pw[int(inst[2]) if not rev else int(inst[-1])]
            pw.pop(int(inst[2]) if not rev else int(inst[-1]))
            pw.insert(int(inst[-1] if not rev else int(inst[2])), m)
    print(''.join(pw))


with open("C:\\Advent\\2016\\day21.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
    pw = [x for x in 'abcdefgh']
    calc(data,pw)
    calc(data[::-1], [x for x in 'fbgdceah'], True)
