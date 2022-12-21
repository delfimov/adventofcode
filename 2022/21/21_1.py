monkeys = {}
for (monkey,yell) in [list(map(str.strip, x.split(':'))) for x in open('input.txt').readlines()]:
    monkeys[monkey] = yell
    if monkeys[monkey].isnumeric():
        monkeys[monkey] = int(yell)
    else:
        monkeys[monkey] = monkeys[monkey].split(' ')

i = 0
equal = monkeys['root']
del monkeys['root']

def solve():
    while True:
        change = False
        for name in monkeys:
            if isinstance(monkeys[name], list):
                if monkeys[name][0] != 'humn' and isinstance(monkeys[name][0], str) and isinstance(monkeys[monkeys[name][0]], int):
                    change = True
                    monkeys[name][0] = monkeys[monkeys[name][0]]
                if monkeys[name][2] != 'humn' and isinstance(monkeys[name][2], str) and isinstance(monkeys[monkeys[name][2]], int):
                    change = True
                    monkeys[name][2] = monkeys[monkeys[name][2]]
                if isinstance(monkeys[name][0], int) and isinstance(monkeys[name][2], int):
                    change = True
                    monkeys[name] = int(eval(f"{monkeys[name][0]} {monkeys[name][1]} {monkeys[name][2]}"))
        if not change:
            break

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
    
def reverse_solve():
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


solve()

del(monkeys['humn'])

if isinstance(monkeys[equal[0]], int):
    key = equal[2]
    val = monkeys[equal[0]]
else:
    key = equal[0]
    val = monkeys[equal[2]]

monkeys = reverse_solve()

monkeys[key] = val
solve()

print(monkeys['humn'])
