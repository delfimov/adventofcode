def get_strength(cycle, x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        print(f"cycle: {cycle}  strength: {x}*{cycle}={x*cycle}")
        return x*cycle
    return 0

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    cycle = 0
    strength_sum = 0
    x = 1
    add_x = 0
    for line in lines:
        command = line.strip().split(' ')
        x += add_x
        add_x = 0
        if command[0].strip() == 'addx':
            cycle += 1
            add_x = int(command[1])
            strength_sum += get_strength(cycle, x)
        cycle += 1
        strength_sum += get_strength(cycle, x)
        # print(f"cycle: {cycle}    command: {command}    x: {x}")
    print(strength_sum)