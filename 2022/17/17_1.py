from itertools import cycle
import collections

# [(w,h), (x1,y1), (x2,y2), ...]


def solve(input_file, cnt):

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
    rocks = {}

    def add_rock(y, shape):
        for dy, line in enumerate(shape):
            posy = y + dy
            if (posy not in rocks):
                rocks[posy] = line
            else:
                rocks[posy] = rocks[posy] | line
        return y+dy

    def is_move(x, y, shape, w):
    #    print(x, x+w)
        if y < 0 or x < 0 or x + w > 7:
    #        print('false')
            return False
        for dy,line in enumerate(shape):
            if y+dy in rocks and rocks[y+dy] & line:
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

    def prepare_jets2(s):
        a = []
        for c in s:
            if c == '<':
                a.append(-1)
            else:
                a.append(1)
        return (len(a), a)

    def prepare_jets(s):
        a = []
        for c in s:
            if c == '<':
                a.append(-1)
            else:
                a.append(1)
        return cycle(enumerate(a))


    history = collections.defaultdict(list)
    jets = prepare_jets(list(open(input_file).read()))
    jet_i = 0
    n = -1
    rocks_height = 0
    height_mod = 0  
    while n < cnt-1:
        n += 1
        shape = next(shapes)
        shape_i = n % 5
        cycle_key = (shape_i, jet_i)
        (w, h) = shape[0]
        shape_value = shape[1:]
        prev_x = x = 2
        prev_y = y = len(rocks) + 3
        while True:
            (jet_i, jet) = next(jets)
            (is_stop, shape_value, x, y) = get_pos(x, y, shape_value, w, h, jet)
            if is_stop:
                # rocks_height = max(rocks_height, add_rock(y, shape_value)+1)
                temph = add_rock(y, shape_value) + 1
                rocks_height = height_mod + temph

                if history is None:
                    break

                key = (cycle_key, x-prev_x, y-prev_y)
                loop_history = history[key]

                if len(loop_history) > 1:
                    prev_y_d = loop_history[-1][0] - loop_history[-2][0]
                    y_d = rocks_height - loop_history[-1][0]

                    if prev_y_d == y_d:
                        loop_delta = n - loop_history[-1][1]

                        remaining_n = cnt - n - 1

                        loop_count = remaining_n // loop_delta
                        skipped_n = loop_count * loop_delta
                        n += skipped_n

                        height_mod = loop_count * y_d

                        rocks_height += height_mod

                        history = None
                        break

                loop_history.append((rocks_height, n))
                break

    return rocks_height


print(solve('input.txt', 2022))
#print_rocks()
print(solve('input.txt', 1000000000000))
