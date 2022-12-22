import re
from collections import deque

facing = deque([(0, '>'), (1, 'v'), (2, '<'), (3, '^')])
coords = [(0, 1), (1, 0), (0, -1), (-1, 0)] # y, x
tiles = []
walls = []
tiles_s, commands = open('input.txt').read().split("\n\n")
size = 0
for line in [[s for s in x] for x in tiles_s.split("\n")]:
    tiles_line = []
    walls_line = []
    for x, c in enumerate(line):
        if c == '.':
            tiles_line.append(x)
        if c == '#':
            tiles_line.append(x)
            walls_line.append(x)
    if size == 0:
        print(tiles_line)
        size = len(tiles_line)
    tiles.append(tiles_line)
    walls.append(walls_line)

commands = list(map(lambda y: int(y) if y.isnumeric() else y, re.findall("(\d+|[R|L]{1})", commands)))

def check_new_pos(x, y, dx, dy):
    new_x, new_y = x + dx, y + dy
    if abs(dy) > 0:
        if new_y >= len(tiles) or new_y < 0 or new_x not in tiles[new_y]:
            while True:
                new_y -= dy
                if new_y >= len(tiles) or new_y < 0 or new_x not in tiles[new_y]:
                    new_y += dy
                    break
    elif abs(dx) > 0:
        if new_x > tiles[new_y][-1]:
            new_x = tiles[new_y][0]
        if new_x < tiles[new_y][0]:
            new_x = tiles[new_y][-1]
    if new_x in walls[new_y]:
        return (True, x, y) # stop
    return (False, new_x, new_y)

x, y = tiles[0][0], 0
#print(x, y, facing[0])
for c in commands:
#    print('f:', facing[0][1], 'c:', c, end='\n')
    if isinstance(c, int):
        for i in range(c):
            (dy, dx) = coords[facing[0][0]]
            (stop, x, y) = check_new_pos(x, y, dx, dy)
            if stop:
                break
    elif c == 'R':
        facing.rotate(-1)
    elif c == 'L':
        facing.rotate(1)
#    print('x,y:', x, y)
#    print()

print(x, y, facing[0])

print((y+1)*1000 + (x+1)*4 + facing[0][0])
