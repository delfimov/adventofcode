#!/usr/bin/env python

import re

rep = dict((l, str(i+1)) for i, l in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))
pattern = re.compile("|".join(rep.keys()))

sum = 0
with open('1.txt') as file:
    for line in file:
        s = pattern.sub(lambda m: rep[re.escape(m.group(0))], line.rstrip())
        s = re.sub('[^0-9]', '', s)
        c = int(s[:1] + s[-1])
        sum += c

print(sum)
