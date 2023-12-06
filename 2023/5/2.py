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
                m.append(m[1]+m[2])
                map.append(m)
    maps.append(map)


locations = []
for i in range(0, len(seeds), 2):
    ranges = [[seeds[i], seeds[i+1] + seeds[i]]]
    results = []
    for map_set in maps[1:]:
        while ranges:
            range_start, range_end = ranges.pop()
            for target, map_start, r, offset, map_end in map_set:
                if map_end <= range_start or range_end <= map_start:
                    continue
                if range_start < map_start:
                    ranges.append([range_start, map_start])
                    range_start = map_start
                if map_end < range_end:
                    ranges.append([map_end, range_end])
                    range_end = map_end
                results.append([range_start + offset, range_end + offset])
                break
            else:
                results.append([range_start, range_end])
        ranges = results
        results = []
    locations += ranges

print(min(l[0] for l in locations))
