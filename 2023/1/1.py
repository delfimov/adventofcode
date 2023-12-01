#!/usr/bin/env python

import re

sum = 0
with open('1.txt') as file:
    for line in file:
        s = re.sub('[^0-9]', '', line.rstrip())
        c = int(s[:1] + s[-1])
        sum += c

print(sum)
