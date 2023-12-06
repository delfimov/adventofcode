#!/usr/bin/env python3

import re

seeds = []
map = []
maps = []
map_name = ''
with open('1.txt') as file:
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
                map.append(m)

    maps.append(map)

for i in range(len(seeds)):
    for map_set in maps[1:]:
        for target, start_map, r, offset in map_set:
            if start_map <= seeds[i] < start_map+r:
                seeds[i] += offset
                break

print(min(seeds))
