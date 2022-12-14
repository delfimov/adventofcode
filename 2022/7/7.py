def command(line):
    out = [False, False]
    line_parts = line.split(' ')
    if line_parts[1] == 'ls':
        out = ['ls', False]
    elif line_parts[1] == 'cd':
        out = ['cd', line_parts[2].strip()]
    return out

def size(line):
    size = 0
    line_parts = line.split(' ')
    if line_parts[0] != 'dir':
        size = int(line_parts[0])
    return size

path = []
sizes = {}

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if line[0:1] == '$':
            cmd = command(line)
            if cmd[0] == 'cd':
                if cmd[1] == '..':
                    path.pop()
                else:
                    path.append(cmd[1])
        else:
            if len(path) > 1:
                count = 0
                for path_part in path[1:]:
                    count += 1
                    path_key = '/' . join(path[1:1+count])
                    if path_key not in sizes:
                        sizes[path_key] = 0
                    sizes[path_key] += size(line)
    sum = 0
    for size in sizes:
        if sizes[size] <= 100000:
            # print(f"{size}: {sizes[size]}")
            sum += sizes[size]
    print(sum)
