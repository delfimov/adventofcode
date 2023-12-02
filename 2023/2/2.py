#!/usr/bin/env python

import re

sum = 0
with open('1.txt') as file:
    for line in file:
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        s = re.split(r' |:|,|;', line.rstrip())
        id = int(s[1])
        for i, word in enumerate(s):
            for cube in cubes:
                if cube == word:
                    if int(s[i-1]) > cubes[cube]:
                        cubes[cube] = int(s[i-1])
        sum += cubes['red']*cubes['green']*cubes['blue']
print(sum)
