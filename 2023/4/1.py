#!/usr/bin/env python

import re

total = 0

colon_pos = 0
bar_pos = 0
with open('1.txt') as file:
    for line in file:
        line = line.rstrip()
        if colon_pos == 0:
            colon_pos = line.find(':')
            bar_pos = line.find('|')
        win = re.split(r' +', line[colon_pos+1:bar_pos].strip())
        my = re.split(r' +', line[bar_pos+1:].strip())
        i = len(set(win).intersection(set(my)))
        if i > 0:
            total += 2**(i-1)
print(total)
