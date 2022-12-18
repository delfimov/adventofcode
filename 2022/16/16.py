import re

valves = {}
for line in [[s for s in re.findall(r'[A-Z]{2}|[\d]+', x)] for x in open('input.txt').readlines()]:
    valves[line[0]] = {'rate': int(line[1]), 'tunnels': line[2:], 'paths': {}}

def bfs(start, end):
    depth = 1
    while True:
        next_start = []
        for x in start:
            if x == end:
                return depth
            for y in valves[x]['tunnels']:
                next_start.append(y)
        start = next_start
        depth += 1

keys = sorted([x for x in list(valves.keys()) if valves[x]['rate'] != 0])

for room in keys + ['AA']:
    for room2 in keys:
        if room2 != room:
            valves[room]['paths'][room2] = bfs(valves[room]['tunnels'], room2)

def search(opened, rate, current_room, minutes, pressure):
    pressure = max(pressure, rate)
    if minutes <= 0:
        return pressure
    if current_room not in opened:
        pressure = max(pressure, search(opened.union([current_room]), rate + valves[current_room]['rate'] * minutes, current_room, minutes - 1, pressure))
    else:
        for room in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
            pressure = max(pressure, search(opened, rate, room, minutes - valves[current_room]['paths'][room], pressure))
    return pressure;

print(search(set(['AA']), 0, 'AA', 29, 0))

def search2(opened, rate, current_room, minutes, pressure, elephants_turn):
    pressure = max(pressure, rate)
    if minutes <= 0:
        return pressure
    if current_room not in opened:
        pressure = max(pressure, search2(opened.union([current_room]), rate + valves[current_room]['rate'] * minutes, current_room, minutes - 1, pressure, elephants_turn))
        if not elephants_turn:
            pressure = max(pressure, search2(set([current_room]).union(opened), rate + valves[current_room]['rate'] * minutes, 'AA', 25, pressure, True))
    else:
        for room in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
            pressure = max(pressure, search2(opened, rate, room, minutes - valves[current_room]['paths'][room], pressure, elephants_turn))
    return pressure

# 307,76s user 0,48s system 99% cpu 5:08,31 total <-- MacBook Air M1 16/512
# print(search2(set(['AA']), 0, 'AA', 25, 0, False))