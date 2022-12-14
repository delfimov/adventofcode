elves = [sum(list(map(int, line.split()))) for line in open("elves.txt").read().split('\n\n')]
print(f"Part 1: elf #{elves.index(max(elves))+1} is carrying {elves[elves.index(max(elves))]} Calories")
print(f"Part 2: three elves with the most calories are carrying {sum(sorted(elves)[-3:])} Calories")
