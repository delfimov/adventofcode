#!/usr/bin/env python3

import re

seeds = []
map = []
maps = []
map_name = ''
with open('test1.txt') as file:
    for line in file:
        line = line.strip()
        if line != '':
            l = re.split(r' +', line.rstrip())
            if l[0] == 'seeds:':
                seeds = [int(x) for x in l[1:]]
            elif l[1] == 'map:':
                maps.append(map)
                map = []
                map_name = l[0]
            else:
                m = [int(x) for x in l]
                m.append(m[0]-m[1])
#                m.append(map_name)
                map.append(m)
    maps.append(map)

min_seed = sys.maxsize
for i in range(0, len(seeds), 2):
    print(seeds[i],'-',seeds[i]+seeds[i+1])
    for x in range(seeds[i], seeds[i]+seeds[i+1]):
        for map_set in maps[1:]:
            for target, start_map, r, offset in map_set:
                if start_map <= x < start_map+r:
                    x += offset
                    break
        if x < min_seed:
            min_seed = x

print(min_seed)
