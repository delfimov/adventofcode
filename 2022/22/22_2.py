import re
import math
from collections import deque

facing = [(1, 0, '>'), (0, 1, 'v'), (-1, 0, '<'), (0, -1, '^')]

tiles, commands = open('input.txt').read().split("\n\n")
tiles = tiles.split("\n")

commands = list(map(lambda y: int(y) if y.isnumeric() else y, re.findall("(\d+|[R|L]{1})", commands)))

s = 0
for line in tiles:
    s += len(line.strip())
s = int(math.sqrt(s/6))

print(s)

def get_pos_x(x, y, d):
    if 0 <= y < s*1:
        if x >= s*3:
            x = s*2-1
            y = s*3-1 - y
            d = (d + 2) % 4
        elif x < s*1:
            x = 0
            y = s*3-1 - y
            d = (d + 2) % 4
    elif s*1 <= y < s*2:
        if x >= s*2:
            x = y + s*1
            y = s*1 - 1
            d = (d + 3) % 4
        elif x < s*1:
            x = y - s*1
            y = s*2
            d = (d + 3) % 4
    elif s*2 <= y < s*3:
        if x >= s*2:
            x = s*3-1
            y = s*3-1 - y
            d = (d + 2) % 4
        elif x < 0:
            x = s*1
            y = s*3-1 - y
            d = (d + 2) % 4
    elif s*3 <= y < s*4:
        if x < 0:
            x = y - s*2
            y = 0
            d = (d + 3) % 4
        elif x >= s*1:
            x = y - s*2
            y = s*3-1
            d = (d + 3) % 4
    return x, y, d


def get_pos_y(x, y, d):
    if 0 <= x < s*1:
        if y < s*2:
            y = x + s*1
            x = s*1
            d = (d + 1) % 4
        elif y >= s*4:
            y = 0
            x += s*2
    elif s*1 <= x < s*2:
        if y < 0:
            y = x + s*2
            x = 0
            d = (d + 1) % 4
        elif y >= s*3:
            y = x + s*2
            x = s*1-1
            d = (d + 1) % 4
    elif s*2 <= x < s*3:
        if y < 0:
            x -= s*2
            y = s*4-1
        elif y >= s*1:
            y = x - s*1
            x = s*2-1
            d = (d + 1) % 4
    return x, y, d

x, y, d = tiles[0].index("."), 0, 0

for c in commands:
    #print(c)
    if isinstance(c, int):
        for i in range(c):
            new_x, new_y = x + facing[d][0], y + facing[d][1]
            if d % 2 == 0:
                new_x, new_y, new_d = get_pos_x(new_x, new_y, d)
            else:
                new_x, new_y, new_d = get_pos_y(new_x, new_y, d)
            if tiles[new_y][new_x] != "#":
                x, y, d = new_x, new_y, new_d
    elif c == 'R':
        d = (d + 1) % 4
    elif c == 'L':
        d = (d + 3) % 4

print(x, y, d)
print((y+1) * 1000 + (x+1) * 4 + d)