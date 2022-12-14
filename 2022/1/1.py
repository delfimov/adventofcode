elves = []
for elf in [map(str.strip, x.split()) for x in open('elves.txt').read().split('\n\n')]:
    elves.append(sum(list(map(int, elf))))
elf = elves.index(max(elves))
print(f"And the answer is: Elf #{elf+1}, he is carrying {elves[elf]} Calories")
print(f"Three elves with the most calories are carrying {sum(sorted(elves)[-3:])} Calories")
