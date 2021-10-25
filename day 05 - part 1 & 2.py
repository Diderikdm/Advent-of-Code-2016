from hashlib import md5

puzzle_input = 'uqwqemis'
x, part1, part2 = 0, 0, 0
password = ''
pass_two = [None for x in range(8)]
prev = []

while len(password) < 8 or any(not y for y in pass_two):
    trial = md5((puzzle_input + str(x)).encode()).hexdigest()
    if trial.startswith('00000'):
        if len(password) < 8:
            password += trial[5]
        if trial[5].isdigit() and int(trial[5]) in range(8) and trial[5] not in prev:
            pass_two[int(trial[5])] = trial[6]
            prev.append(trial[5])
    x+=1

print(password)
print(''.join(pass_two))
