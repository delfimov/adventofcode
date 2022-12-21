monkeys = {}
for (monkey,yell) in [list(map(str.strip, x.split(':'))) for x in open('input.txt').readlines()]:
    monkeys[monkey] = yell
    if monkeys[monkey].isnumeric():
        monkeys[monkey] = int(yell)
    else:
        monkeys[monkey] = monkeys[monkey].split(' ')

i = 0
while True:
    for name in monkeys:
        # monkey = monkeys[name]
        if isinstance(monkeys[name], list):
            if isinstance(monkeys[name][0], str) and isinstance(monkeys[monkeys[name][0]], int):
                monkeys[name][0] = monkeys[monkeys[name][0]]
            if isinstance(monkeys[name][2], str) and isinstance(monkeys[monkeys[name][2]], int):
                monkeys[name][2] = monkeys[monkeys[name][2]]
            if isinstance(monkeys[name][0], int) and isinstance(monkeys[name][2], int):
                monkeys[name] = int(eval(f"{monkeys[name][0]} {monkeys[name][1]} {monkeys[name][2]}"))
    if isinstance(monkeys['root'], int):
        break
print(monkeys['root'])
