from functools import reduce

def is_right(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return None if l == r else l < r

    if isinstance(l, list) and isinstance(r, list):
        for left, right in zip(l, r):
            if (comparison := is_right(left, right)) is not None:
                return comparison
        return is_right(len(l), len(r))

    return is_right([l], r) if isinstance(l, int) else is_right(l, [r])


total = 0
packets = []
for i, (l,r) in enumerate([map(eval, x.split()) for x in open('input.txt').read().split('\n\n')]):
    packets.append(l)
    packets.append(r)
    print()
    print('===== Pair', i+1, '=====')
    answer = is_right(l, r)
    print(answer)
    if answer:
        total += i+1
print(total)

print()

position_1_reduce = reduce(lambda s,p: s+1 if is_right(p, [[2]]) else s+0, packets, 1)
position_2_reduce = reduce(lambda s,p: s+1 if is_right(p, [[6]]) else s+0, packets, 2)

position_1_sum = 1 + sum(1 for p in packets if is_right(p, [[2]]))
position_2_sum = 2 + sum(1 for p in packets if is_right(p, [[6]]))


print(position_1_reduce * position_2_reduce)

print(position_1_sum * position_2_sum)

