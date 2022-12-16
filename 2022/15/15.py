import re

def is_valid(x, y, lines):
    for (sx, sy, size) in lines:
        if abs(y - sy) + abs(x - sx) <= size:
            return False
    return True

def find_part2(lines):
    for (sx, sy, size) in lines:
        # проверять только на расстоянии d+1 от sx sy
        for dx in range(size + 2):
            dy = size + 1 - dx
            for (signx, signy) in [(1,1), (-1,1), (1,-1), (-1,-1)]:
                x = sx + dx * signx
                y = sy + dy * signy
                if not(0 <= x <= 4000000 and 0 <= y <=4000000):
                    continue
                if is_valid(x, y, lines):
                    return x * 4000000 + y

x1 = 999999999
x2 = -999999999
line = 2000000
lines = []

for sx, sy, bx, by in [[int(s) for s in re.findall(r'[\-\d]+', x)] for x in open('input.txt').readlines()]:
    size = abs(sx - bx) + abs(sy - by)
    d = 0
#    print('coords:', sy, sx, by, bx)
    if (line >= sy >= line - size) or (line < sy <= line + size):
        d = size - abs(sy - line)
        x1 = min(x1, sx - d)
        x2 = max(x2, sx + d)
    lines.append((sx, sy, size))

print(abs(x1-x2))

print(find_part2(lines))
