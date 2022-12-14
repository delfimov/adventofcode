head = [0, 0]
tail = [0, 0]
visited = [tail[:]]
visited_count = 1

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
            visited.append(tail[:])
            tail = move_tail(head, tail)
            if tail not in visited:
                visited_count += 1
    print(visited_count)
