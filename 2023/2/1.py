#!/usr/bin/env python

import re

sum = 0
cubes = {'red': 12, 'green': 13, 'blue': 14}
with open('1.txt') as file:
    for line in file:
        s = re.split(r' |:|,|;', line.rstrip())
        #print(s)
        id = int(s[1])
        for i, word in enumerate(s):
            for cube in cubes:
                if cube == word:
                    if cubes[cube] < int(s[i-1]):
                        id = 0
                        break
                    #print(f'Game {id}. {cube}: max: {cubes[cube]}, index {i} value: {s[i-1]}')
            else:
                continue
            break
        sum += id
print(sum)
