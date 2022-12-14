import math

monkeys = []
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    items = []
    test = 0
    test_false = -1
    test_true = -1
    operation = []
    monkey = {}
    modulo = 1
    for line in lines:
        command = line.strip().split(' ')
        if command[0]:
            print(command)
            if command[0] == 'Monkey':
                monkey_n = int(command[1].strip(':'))
            elif command[0] == 'Starting':
                for item_n in command[2:]:
                    items.append(int(item_n.strip(', ')))
                monkey['items'] = items
            elif command[0] == 'Operation:':
                operation = command[3:]
                monkey['operation'] = operation
            elif command[0] == 'Test:':
                test = int(command[3])
                monkey['test'] = test
            elif command[0] == 'If' and command[1] == 'true:':
                test_true = int(command[5])
                monkey['test_true'] = test_true
            elif command[0] == 'If' and command[1] == 'false:':
                test_false = int(command[5])
                monkey['test_false'] = test_false
        else:
            monkey['times'] = 0
            modulo *= test
            monkeys.append(monkey)
            monkey = {}
            print(f"Monkey: {monkey_n}; items: {items}; operation: {operation}; If divisable by {test} ? {test_true} : {test_false}")
            items = []
            test = 0
            test_false = -1
            test_true = -1
            operation = []

    for i in monkeys:
        print(i)



    for i in range(0, 10000):
        for monkey in monkeys:
            for item in monkey['items']:
                if monkey['operation'][0] == 'old':
                    multiply1 = item
                else:
                    multiply1 = int(monkey['operation'][0])
                if monkey['operation'][2] == 'old':
                    multiply2 = item
                else:
                    multiply2 = int(monkey['operation'][2])
                if monkey['operation'][1] == '*':
                    worry_level = multiply1 * multiply2
                elif monkey['operation'][1] == '+':
                    worry_level = multiply1 + multiply2
                # worry_level = math.floor(worry_level / 3)
                # a = worry_level // monkey['test'] 
                #if a == worry_level:
                worry_level = worry_level % modulo
                if worry_level % monkey['test'] == 0:
                    monkeys[monkey['test_true']]['items'].append(worry_level)
                else:
                    monkeys[monkey['test_false']]['items'].append(worry_level)
                monkey['times'] += 1
            monkey['items'] = []
    print()
    print()
    monkeys_sorted = monkeys
    monkeys_sorted = sorted(monkeys, key=lambda d: d['times'], reverse=True) 
    for i in monkeys_sorted:
        print(i)

    print(monkeys_sorted[0]['times'] * monkeys_sorted[1]['times'])