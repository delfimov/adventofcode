head = [0, 0]
tail = [0, 0]
tails = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
]
visited = {
    0: [0]
}
visited_count = 0

def move_tail(head, tail):
    moveX = 0
    moveY = 0
    head_to_tail_x = abs(head[0]-tail[0])
    head_to_tail_y = abs(head[1]-tail[1])
    if head_to_tail_x > 1 or (head_to_tail_y > 1 and head_to_tail_x > 0):
        moveX = 1 if head[0] > tail[0] else -1
    if head_to_tail_y > 1 or (head_to_tail_x > 1 and head_to_tail_y > 0):
        moveY = 1 if head[1] > tail[1] else -1
    return [tail[0]+moveX, tail[1]+moveY]

def add_visited(visited, tail):
    if tail[1] not in visited:
        visited[tail[1]] = []
    if tail[0] not in visited[tail[1]]:
        visited[tail[1]].append(tail[0])
    return visited


with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        command = line.strip().split(' ')
        for i in range(1, int(command[1])+1):
            direction = command[0]
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            prev_tail = head
            for i in range(0, 9):
                tails[i] = move_tail(prev_tail, tails[i])
                prev_tail = tails[i]
            visited = add_visited(visited, tails[i])

    max_length = 0
    start = 0
    for line in visited:
        if max(visited[line]) > max_length:
            max_length = max(visited[line])
        if min(visited[line]) < start:
            start = min(visited[line])

    keys = reversed(sorted(visited.keys()))
    for line in keys:
        visited_count += len(visited[line])
        #for char in range(start, max_length+1):
        #    if (char in visited[line]):
        #        print('#', end='')
        #    else:
        #        print('.', end='')
        #print()

    print(visited_count)
