import re

min_x = min_y = x1 = 999999999
max_x = max_y = x2 = -999999999
line = 2000000
lines = set() # set is faster than list

def is_valid(x, y, lines):
    for (sx, sy, size) in lines:
        dxy = abs(y - sy) + abs(x - sx)
        if dxy <= size:
            return False
    return True

for i, (sx, sy, bx, by) in enumerate([[int(s) for s in re.findall(r'[\-\d]+', x)] for x in open('input.txt').readlines()]):
    size = abs(sx - bx) + abs(sy - by)
    d = 0
#    print('coords:', sy, sx, by, bx)
    if (line >= sy >= line - size) or (line < sy <= line + size):
        d = size - abs(sy - line)
        x1 = min(x1, sx - d)
        x2 = max(x2, sx + d)
    min_x = min(min_x, sx, bx)
    min_y = min(min_y, sy, by)
    max_x = max(max_x, sx, bx)
    max_y = max(max_y, sy, by)
    lines.add((sx,sy,size))

print(abs(x1-x2))

count = 0
p2 = None
for (sx,sy,size) in lines:
    # проверять только на расстоянии d+1 от sx sy
    for dx in range(size + 2):
        dy = (size + 1) - dx
        for signx,signy in [(1,1), (-1,1), (1,-1), (-1,-1)]:
            count += 1
            x = sx + (dx*signx)
            y = sy + (dy*signy)
            if not(0 <= x <= 4000000 and 0 <= y <=4000000):
                continue
            assert abs(x-sx) + abs(y-sy) == size + 1
            if is_valid(x,y,lines) and p2 is None:
                p2 = x*4000000 + y
                break
        if p2 is not None:
            break
    if p2 is not None:
        break
# print(count)             
print(p2)