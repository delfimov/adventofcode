head = [0, 0]
tail = [0, 0]
visited = [tail[:]]
visited_count = 1

def move_tail(head, tail, distance):
    moveX = 0
    moveY = 0
    head_to_tail_x = abs(head[0]-tail[0])
    head_to_tail_y = abs(head[1]-tail[1])
    if head_to_tail_x > 1:
        moveX = distance if head[0] > tail[0] else -distance
    elif head_to_tail_y > 1 and head_to_tail_x > 0:
        moveX = 1 if head[0] > tail[0] else -1
    if head_to_tail_y > 1:
        moveY = distance if head[1] > tail[1] else -distance
    elif head_to_tail_x > 1 and head_to_tail_y > 0:
        moveY = 1 if head[1] > tail[1] else -1
    return [tail[0]+moveX, tail[1]+moveY]

def add_visited(visited, tail):
    if tail not in visited:
        visited.append(tail[:])
    return visited

def add_travel(visited, tail_before, tail_after):
    tail_x = tail_before[0]-tail_after[0]
    tail_y = tail_before[1]-tail_after[1]
    if abs(tail_x) > abs(tail_y):
#        print('--------')
#        print(tail_before)
#        print(tail_after)
#        print(f"abs(tail_x)+1: {abs(tail_x)+1}")
        for i in range(1, abs(tail_x)+1):
#            print([tail_before[0]+i, tail_before[1]+tail_y])
            visited = add_visited(visited, [tail_before[0]+i, tail_before[1]+tail_y])
    else:
#        print('--------')
#        print(tail_before)
#        print(tail_after)
#        print(f"abs(tail_y)+1: {abs(tail_y)+1}")
        for i in range(1, (tail_y)+1):
#            print([tail_before[0]+tail_x, tail_before[1]+i])
            visited = add_visited(visited, [tail_before[0]+tail_x, tail_before[1]+i])
    return visited


with open('test.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        command = line.strip().split(' ')
        distance = int(command[1])
        direction = command[0]
        if direction == 'R':
            head[0] += distance
        elif direction == 'L':
            head[0] -= distance
        elif direction == 'U':
            head[1] += distance
        elif direction == 'D':
            head[1] -= distance
        # visited.append(tail[:])
        tail_new = move_tail(head, tail, distance-1)
        visited = add_travel(visited, tail, tail_new)
        tail = tail_new
        # print(visited)
        #if tail not in visited:
        #    visited_count += 1
        # print(f"line: {line.strip()};   head: {head[0]}:{head[1]} - tail: {tail[0]}:{tail[1]}")
    # print(visited)
    print(len(visited))
    print(head)
    print(tail)