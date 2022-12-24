dirs = ((1,0),(0,1),(-1,0),(0,-1),(0,0)) # y, x

def show_valley(valley):
    s = '\n'.join([''.join(map(str, x)) for x in valley])
    print(s)

valley = [list(x) for x in open('input.txt').read().split("\n")]
show_valley(valley)

h = len(valley) - 2
w = len(valley[0]) - 2

moves = {
    "<": (0, -1), 
    ">": (0, 1), 
    "v": (1, 0), 
    "^": (-1, 0)
    }

blizzard = []
for y in range(1, h+1):
    for x in range(1, w+1):
        if valley[y][x] != ".":
            blizzard.append([(y, x), moves[valley[y][x]]])

def next_minute():
    positions = set()
    for state in blizzard:
        (y, x), (dy, dx) = state
        new_y = ((y + dy - 1) % h) + 1
        new_x = ((x + dx - 1) % w) + 1
        state[0] = (new_y, new_x) 
        positions.add((new_y, new_x))
    return positions

rounds = [
    ((0,1), (h+1,w), 0), 
    ((h+1,w), (0,1), 1), 
    ((0,1), (h+1,w), 1)
    ]

parts = []

for round in rounds:
    start, finish, dm = round
    path = [(start, dm)]
    visited = set() # sets are faster than lists for search 
    max_d = -1
    while True:
        (cy,cx),minute = path.pop(0)
        if (cy,cx) == finish:
            parts.append(minute)
            break
        if minute > max_d:
            max_d = minute
            blizzards = next_minute()
        for dy, dx in dirs:
            new_y = cy + dy
            new_x = cx + dx
            if (new_y,new_x,minute) not in visited and (
                    (1 <= new_y <= h and 1 <= new_x <= w and (new_x,new_y) not in blizzards)
                    or (new_y,new_x) == start or (new_y,new_x) == finish or (
                    )
                ):
                    visited.add((new_y,new_x,minute))
                    path.append(((new_y,new_x), minute+1))
            
print(parts)
print(sum(parts))
