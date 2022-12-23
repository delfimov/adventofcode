from collections import deque

def show_scan(scan):
    for line in scan:
        for c in line:
            print(c, end='')
        print()

def add_lines(scan):
    add_before = add_after = False
    for line in scan:
        if line[0] == '#':
            add_before = True
        if line[-1] == '#':
            add_after = True
    for line in scan:
        if add_before:
            line.insert(0, '.')
        if add_after:
            line.append('.')
    if '#' in scan[0]:
        scan.insert(0, ['.'] * len(scan[0]))
    if '#' in scan[-1]:
        scan.append(['.'] * len(scan[0]))
    return scan

def count_space(scan):
    first_y = first_x = 100000
    last_y = last_x = 0
    elves = 0
    for y,line in enumerate(scan):
        for x,c in enumerate(line):
            if c == '#':
                elves += 1
                first_x = min(x, first_x)
                first_y = min(y, first_y)
                last_x = max(x, last_x)
                last_y = max(y, last_y)
    return (last_x-first_x+1)*(last_y-first_y+1) - elves

scan = [list(x) for x in open('input.txt').read().split("\n")]
dir = deque([
    [(-1, 0), (-1, 1), (-1, -1)], # N, NE, NW / y, x
    [(1, 0), (1, 1), (1, -1)],    # S, SE, SW
    [(0, -1), (-1, -1), (1, -1)], # W, NW, SW
    [(0, 1), (1, 1), (-1, 1)],    # E, NE, SE
])

show_scan(scan)

i = 0
while True:
#    print('before', len(scan[0]))
    scan = add_lines(scan)
    moves = {}
    cancelled = {}
#    print('after', len(scan[0]))
    for y,line in enumerate(scan):
        for x,c in enumerate(line):
            if c == '#':
                move = False
                dy = None
                for d, ((dy1,dx1), (dy2,dx2), (dy3,dx3)) in enumerate(dir):
                    if scan[y+dy1][x+dx1] == '#' or scan[y+dy2][x+dx2] == '#' or scan[y+dy3][x+dx3] == '#':
                        move = True
                    elif scan[y+dy1][x+dx1] != '#' and scan[y+dy2][x+dx2] != '#' and scan[y+dy3][x+dx3] != '#':
                        if dy is None:
                            dy = dy1
                            dx = dx1
                if move and dy is not None:
                    new_y = y+dy
                    new_x = x+dx
                    if (new_y,new_x) in moves:
                        cancelled[(new_y,new_x)] = moves[(new_y,new_x)]
                    else:
                        moves[(new_y,new_x)] = (y,x)

    for (new_y,new_x) in cancelled:
        del(moves[(new_y,new_x)])
    for (new_y,new_x) in moves:
        (y,x) = moves[(new_y,new_x)]
        scan[y][x] = '.'
        scan[new_y][new_x] = '#'
    i += 1
    if len(moves) == 0:
        break
    dir.rotate(-1)

show_scan(scan)
print(i)

#scan[0][0] = '#'
#scan = add_lines(scan)

print(count_space(scan))
