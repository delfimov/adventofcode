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
            if len(path) > 0:
                count = 0
                for path_part in path[0:]:
                    count += 1
                    path_key = '/' . join(path[0:count])
                    if path_key not in sizes:
                        sizes[path_key] = 0
                    sizes[path_key] += size(line)
    sum = 0
    sizes
    free_space = 70000000 - sizes['/']
    required_space = 30000000
    extra_free_space = required_space-free_space
    to_delete = []
    for size in sizes:
        if sizes[size] >= extra_free_space:
            to_delete.append(sizes[size])
    print(min(to_delete))

