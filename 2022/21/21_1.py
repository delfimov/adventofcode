
def solve(monkeys):
    while True:
        change = False
        for name in monkeys:
            if isinstance(monkeys[name], list):
                if monkeys[name][0] in monkeys and isinstance(monkeys[name][0], str) and isinstance(monkeys[monkeys[name][0]], int):
                    change = True
                    monkeys[name][0] = monkeys[monkeys[name][0]]
                if monkeys[name][2] in monkeys and  isinstance(monkeys[name][2], str) and isinstance(monkeys[monkeys[name][2]], int):
                    change = True
                    monkeys[name][2] = monkeys[monkeys[name][2]]
                if isinstance(monkeys[name][0], int) and isinstance(monkeys[name][2], int):
                    change = True
                    monkeys[name] = int(eval(f"{monkeys[name][0]} {monkeys[name][1]} {monkeys[name][2]}"))
        if not change:
            break
    return monkeys

def get_new_action(x, y, op, pos):
    if op == '/' and pos == 1:
        return [y, '/', x]
    elif op == '/' and pos == 2:
        return [y, '*', x]
    elif op == '*':
        return [x, '/', y]
    elif op == '+':
        return [x, '-', y]
    elif op == '-' and pos == 1:
        return [y, '-', x]
    elif op == '-' and pos == 2:
        return [y, '+', x]
    
def reverse_solve(monkeys):
    new_monkeys = {}
    for name in monkeys:
        if isinstance(monkeys[name], list):
            op = monkeys[name][1]
            if isinstance(monkeys[name][0], int):
                key2 = monkeys[name][2]
                val2 = monkeys[name][0]
                new_monkeys[key2] = get_new_action(name, val2, op, 1)
            else:
                key2 = monkeys[name][0]
                val2 = monkeys[name][2]
                new_monkeys[key2] = get_new_action(name, val2, op, 2)
        else:
            new_monkeys[name] = monkeys[name]
    return new_monkeys

def get_monkeys(input_file):
    monkeys = {}
    for (monkey,yell) in [list(map(str.strip, x.split(':'))) for x in open(input_file).readlines()]:
        monkeys[monkey] = yell
        if monkeys[monkey].isnumeric():
            monkeys[monkey] = int(yell)
        else:
            monkeys[monkey] = monkeys[monkey].split(' ')
    return monkeys


part1 = solve(get_monkeys('test.txt'))
print('Part 1:', part1['root'])

part2 = get_monkeys('input.txt')
del(part2['humn'])
part2 = solve(part2)
root = part2['root']
del(part2['root'])
part2 = reverse_solve(part2)
part2[root[0]] = root[2]
part2 = solve(part2)

print('Part 2:', part2['humn'])
