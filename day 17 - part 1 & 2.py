from hashlib import md5

def walk(data, path = [], coord = (0,0), steps = 0):
    if coord == (3,3):
        paths.append(''.join(path))
        return
    ods = [dirs[e] for e,x in enumerate(md5((data + ''.join(path)).encode()).hexdigest()[:4]) if x in opns and vald[dirs[e]](*coord)]
    for od in ods:
        walk(data, path+[od], crds[od](*coord), steps+1)

data = 'njfxhljp'
vald = {'U' : lambda x,y : y > 0, 'D' : lambda x,y : y < 3, 'L' : lambda x,y : x > 0, 'R' : lambda x,y : x < 3}
crds = {'U' : lambda x,y : (x,y-1), 'D' : lambda x,y : (x,y+1), 'L' : lambda x,y : (x-1,y), 'R' : lambda x,y : (x+1,y)}
dirs = ['U', 'D', 'L', 'R']
opns = ['b', 'c', 'd', 'e', 'f']
paths = []
walk(data)
print(sorted(paths, key = lambda x: len(x))[0])
print(len(sorted(paths, key = lambda x: -len(x))[0]))
