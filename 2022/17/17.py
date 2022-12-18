from itertools import cycle

# [(w,h), (x1,y1), (x2,y2), ...]
shapes = cycle([
    [
        (4,1), 
        0b0111100
    ],
    [
        (3,3), 
        0b0001000, 
        0b0011100, 
        0b0001000, 
    ],
    [
        (3,3), 
        0b0011100, 
        0b0010000, 
        0b0010000, 
    ],
    [
        (1,4), 
        0b0000100, 
        0b0000100, 
        0b0000100, 
        0b0000100, 
    ],
    [
        (2,2), 
        0b0001100, 
        0b0001100, 
    ]
])
rocks = []

empty_line = 0b0000000

def add_rock(y, shape, h):
    if len(rocks) < y+h:
        for i in range(len(rocks), y+h):
            rocks.append(empty_line)
    for dy, line in enumerate(shape):
        posy = y + dy
        rocks[posy] = rocks[posy] | line

def is_move(x, y, shape, w):
#    print(x, x+w)
    if y < 0 or x < 0 or x + w > 7:
#        print('false')
        return False
    for dy,line in enumerate(shape):
        if len(rocks) > y+dy and rocks[y+dy] & line:
            return False
    return True

def get_new_shape(shape, dx):
    new_shape = []
    if dx > 0:
        for line in shape:
            new_shape.append(line<<1)
    else:
        for line in shape:
            new_shape.append(line>>1)
    return new_shape

def get_pos(x, y, shape, w, h, dx):
    is_stop = False
    new_shape = get_new_shape(shape, dx)
    posx = x + dx
    if not is_move(posx, y, new_shape, w):
        new_shape = shape
        posx = x
    posy = y
    if is_move(posx, y - 1, new_shape, w):
        posy = y - 1
    else:
        is_stop = True
    return (is_stop, new_shape, posx, posy)

def print_rocks():
    for y in range(len(rocks)+2, -1, -1):
        if y < len(rocks):
            print('|', end='')
            for x in range(0, 7):
                if rocks[y] & (1 << x):
                    print('#', end='')
                else:
                    print('.', end='')
            print('|', end='')
            print()
        else:
            print('|.......|')

patterns = []

def prepare_jets(s):
    a = []
    for c in s:
        if c == '<':
            a.append(-1)
        else:
            a.append(1)
    return cycle(a)

jets = prepare_jets(list(open("input.txt").read()))


def solve(cnt):
    for n in range(0, cnt):
        shape = next(shapes)
        (w, h) = shape[0]
        shape_value = shape[1:]
        x = 2
        y = len(rocks) + 3
        while True:
            jet = next(jets)
            (is_stop, shape_value, x, y) = get_pos(x, y, shape_value, w, h, jet)
            if is_stop:
                add_rock(y, shape_value, h)
                break
    return len(rocks)


print(solve(2022))
print_rocks()
print(len(rocks))
