def fill_disk(data, limit):
    while len(data) < limit:
        data = data + [0] + [int(not(x)) for x in data[::-1]]
    checksum = data[:limit]
    while len(checksum) % 2 == 0:
        checksum = [int(not sum(checksum[x:x+2]) == 1) for x in range(0, len(checksum), 2)]
    return checksum

data = [int(x) for x in '00101000101111010']
for limit in [272, 35651584]:
    print(''.join([str(x) for x in fill_disk(data[:], limit)]))
