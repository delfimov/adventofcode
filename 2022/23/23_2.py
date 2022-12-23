from collections import deque
from PIL import Image, ImageDraw, ImageFont

def show_scan(scan):
    s = '\n'.join([''.join(map(str, x)) for x in scan])
    print(s)

f = ImageFont.truetype('RobotoMono-Bold.ttf', 8)
def save_scan(i, scan):
    s = '\n'.join([''.join(x) for x in scan])
    #f = open(f"slides/{i}.txt", "w")
    #f.write(s)
    #f.close()
    img = Image.new('RGB', (1080, 1920), (0,0,0))
    d = ImageDraw.Draw(img)
    d.text((170, 50), s, fill=(255, 255, 255),font=f)
    i = str(i).rjust(4, '0')
    img.save(f"slides/{i}.png", 'png')
    print(i)

def add_lines(scan):
    for i in range(25):
        for line in scan:
            line.insert(0, '.')
    for i in range(60):
        for line in scan:
            line.append('.')
    for i in range(15):
        scan.insert(0, ['.'] * len(scan[0]))
    for i in range(55):
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

scan = add_lines(scan)

i = 0
while True:
#    print('before', len(scan[0]))
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
    save_scan(i, scan)
    if len(moves) == 0:
        break
    dir.rotate(-1)

show_scan(scan)
print(i)

#scan[0][0] = '#'
#scan = add_lines(scan)

print(count_space(scan))
