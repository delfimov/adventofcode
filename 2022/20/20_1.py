# numbers = [(x, i) for (i, x) in enumerate(int(x.strip()) for x in open('input.txt').readlines())]
numbers = list(enumerate(811589153*int(x.strip()) for x in open('input.txt').readlines()))

numbers_len = len(numbers)

for mix in range(10):
    for move_n in range(numbers_len):
        for current_pos in range(numbers_len):
            if move_n == numbers[current_pos][0]:
                break
        (old_pos, val) = numbers.pop(current_pos)
        current_pos = (current_pos + val) % (numbers_len - 1)
        numbers.insert(current_pos, (move_n, val))
        # print([x[0] for x in numbers])

for zero_pos in range(numbers_len):
    if numbers[zero_pos][1] == 0:
        break

print(sum([numbers[(zero_pos + pos) % numbers_len][1] for pos in [1000, 2000, 3000]]))
