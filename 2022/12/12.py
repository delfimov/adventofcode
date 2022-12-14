grid = [list(map(ord, line.strip())) for line in open("input.txt").readlines()]
h = len(grid)
w = len(grid[0])

start, end = [[(y, x) for x in range(w) for y in range(h) if grid[y][x] == c][0] for c in (ord("S"), ord("E"))]

grid[start[0]][start[1]] = ord("a")
grid[end[0]][end[1]] = ord("z")

path = [(0, start)]
seen = set()
path_length = 0
max_path_length = 0
i = 0
while True:
    if max_path_length < len(path):
        max_path_length = len(path)
    loop, position = path.pop(0)
    if position in seen:
        continue
    seen.add(position)
    y, x = position
    if position == end:
        path_length = loop
        break
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and (ny, nx) not in seen and (grid[y][x] - grid[ny][nx]) <= 1:
            path.append((loop + 1, (ny, nx)))
            i += 1

print(path_length)
print(i)