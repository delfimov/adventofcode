def next_step(cave, x, y):
    if x in cave[y] or y+1 >= len(cave):
        return [True, cave]
    if x not in cave[y+1]:
        return next_step(cave, x, y+1)
    elif x-1 not in cave[y+1]:
        return next_step(cave, x-1, y+1)
    elif x+1 not in cave[y+1]:
        return next_step(cave, x+1, y+1)
    else:
        cave[y].append(x)
    return [False, cave]

cave = []
for command in [list(map(str.strip, x.split('->'))) for x in open('input.txt').readlines()]:
    prev = None
    for (x,y) in list(map(lambda x: map(int, x.split(',')), command)):
        for pos_y in range(0, y+1):
            for pos_x in range(0, x+1):
                if len(cave) <= pos_y:
                    cave.append([])
                if y == pos_y and x == pos_x: 
                    cave[pos_y].append(x)
        if prev is not None:
            for add_y in range(prev[1], y, -1 if prev[1] > y else 1):
                if x not in cave[add_y]:
                    cave[add_y].append(x)
            for add_x in range(prev[0], x, -1 if prev[0] > x else 1):
                if add_x not in cave[y]:
                    cave[y].append(add_x)
        prev = (x, y)

cave2 = cave.copy()

sand = 0
(x, y) = (500, 0)
while True:
    (result, cave) = next_step(cave, x, y)
    if result:
        break
    sand += 1
print('Part 1', sand)

cave2.append([])
cave2.append([])

for floorx in range(0,1000):
    cave2[len(cave2)-1].append(floorx)

(x, y) = (500, 0)
while True:
    (result, cave2) = next_step(cave2, x, y)
    if result:
        break
    sand += 1
print('Part 2', sand)
