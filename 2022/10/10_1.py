def get_line(cycle, line, x):
    cycle_x = cycle % 40
    if cycle_x == 1:
        print(line)
        line = ''
    # print(f"cycle: {cycle}   cycle_x: {cycle_x}   x: {x}")
    cycle_x -= 1
    if cycle_x == x or cycle_x == x-1 or cycle_x == x+1:
        line += '#'
    else:
        line += '.'
    return line

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    cycle = 0
    crt_line = ''
    x = 1
    add_x = 0
    for line in lines:
        command = line.strip().split(' ')
        x += add_x
        add_x = 0
        if command[0].strip() == 'addx':
            cycle += 1
            add_x = int(command[1])
            crt_line = get_line(cycle, crt_line, x)
        cycle += 1
        crt_line = get_line(cycle, crt_line, x)
        # print(f"cycle: {cycle}    command: {command}    x: {x}")
    print(crt_line)