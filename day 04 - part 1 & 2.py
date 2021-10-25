with open("C:\\Advent\\2016\\day4.txt", 'r') as file:
    data = [x for x in file.read().splitlines()]
    alphabet = [x for x in range(ord('a'), ord('z')+1)]
    sum_rooms = 0
    real = {}
    for room in data:
        raw, ans = [x.strip(']') for x in room.split('[')]
        raw_data = raw.split('-')
        id_ = int(raw_data[-1])
        raw_list = [x for x in ''.join(raw_data[:-1])]
        room_ans = []
        for z in sorted([x for x in raw_list], key=lambda y: (-raw_list.count(y), ord(y))):
            if z not in room_ans and len(room_ans) < 5:
                room_ans.append(z)
        if ''.join(room_ans) == ans:
            sum_rooms += id_
            real[' '.join([''.join([chr(alphabet[(alphabet.index(ord(x))+id_)%26]) for x in word]) for word in raw_data[:-1]])] = id_
    print(sum_rooms)
    print(next(iter(v for k,v in real.items() if 'northpole object' in k), None))
