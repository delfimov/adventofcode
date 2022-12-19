priorities = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    count = 0
    badges_sum = 0
    elves_group = []
    for line in lines:
        count = count + 1
        line_clean = line.strip()
        elves_group.append(line_clean)
        is_found = False
        if count == 3:
            count = 0
            print(elves_group)
            for item in elves_group[0]:
                if item in elves_group[1] and item in elves_group[2] and not is_found:
                    badges_sum = badges_sum + priorities.find(item)
                    is_found = True
                    print(f"{item} - {priorities.find(item)} - {badges_sum}")
            elves_group = []
    print(badges_sum)
