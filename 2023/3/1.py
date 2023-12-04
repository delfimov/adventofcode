#!/usr/bin/env python

import re

sum = 0
lines = []
search = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
    )

with open('1.txt') as file:
    for line in file:
        s = re.split(r'([0-9]+)', line.rstrip())
        line2 = []
        for c in s:
            if c != '':
                for cpart in list(c):
                    if c.isnumeric():
                        line2.append(c)
                    else:
                        line2.append(cpart)
        lines.append(line2)

lines_len = len(lines)
line_len = len(lines[0])
for l, line in enumerate(lines):
#    print(f'{l}: ', end='')
    prev_n = -1
    prev_line = -1
    for p, c in enumerate(line):
        if c != '.' and not c.isnumeric():
            for delta in search:
                if l+delta[0] >= 0 and l+delta[0] < lines_len and \
                    p+delta[1] >= 0 and p+delta[1] < line_len and \
                    lines[l+delta[0]][p+delta[1]].isnumeric():
                        if prev_line != l+delta[0]:
                            prev_n = -1
                        prev_line = l+delta[0]
                        if prev_n != int(lines[l+delta[0]][p+delta[1]]):
                            prev_n = int(lines[l+delta[0]][p+delta[1]])
                            sum += prev_n
#                            print(prev_n, end=', ')
                else:
                    prev_n = -1
#    print()
print(sum)
