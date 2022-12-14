grid = [list(map(ord, line.strip())) for line in open("input.txt").readlines()]
h = len(grid)
w = len(grid[0])

start, end = [[(y, x) for x in range(w) for y in range(h) if grid[y][x] == c][0] for c in (ord("S"), ord("E"))]

grid[start[0]][start[1]] = ord("a")
grid[end[0]][end[1]] = ord("z")

path = [(0, end)]
seen = set()
path_length = 0
path_length2 = 0
i = 0
while True:
    loop, position = path.pop(0)
    if position in seen:
        continue
    seen.add(position)
    y, x = position
    if grid[y][x] == ord("a"):
        if not path_length2:
            path_length2 = loop
        elif position == start:
            path_length = loop
            break
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny = y + dy
        nx = x + dx
        if 0 <= ny < h and 0 <= nx < w and (ny, nx) not in seen and (grid[y][x] - grid[ny][nx]) <= 1:
            path.append((loop + 1, (ny, nx)))
            i += 1

print(i)
print(path_length, path_length2)