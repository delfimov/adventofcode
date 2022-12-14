step = 1
stacks = {}

def add_to_stack(stacks: list, line: str):
    step = 4
    count = 1
    i = 1
    while i < len(line) and line[0] == '[':
        if count not in stacks:
            stacks[count] = []
        letter = line[i:i+1]
        if letter != ' ':
            stacks[count].append(line[i:i+1])
        i += step
        count += 1
    return stacks

def move(stacks: list, line: str):
    actions = line.split(' ')
    if actions[0] == 'move' and actions[2] == 'from' and actions[4] == 'to':
        move_count = actions[1]
        move_from = actions[3]
        move_to = actions[5]
        print(f"{line}: {move_count}: {move_from} -> {move_to}")
        part = stacks[int(move_from)][0:int(move_count)]
        # part.reverse()
        stacks[int(move_to)] = part + stacks[int(move_to)]
        stacks[int(move_from)] = stacks[int(move_from)][int(move_count):]
    return stacks

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == '':
            for stack in stacks:
                print(stacks[stack])
            print("\n")
            step = 2
        elif step == 1:
            stacks = add_to_stack(stacks, line)
        elif step == 2:
            stacks = move(stacks, line)

    for stack in stacks:
        print(stacks[stack])
