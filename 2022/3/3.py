priorities = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
    count = 0
    items_sum = 0
    for line in lines:
        count = count + 1
        line_clean = line.strip()
        length = len(line_clean)
        compartment1 = line_clean[0:int(length/2)]
        compartment2 = line_clean[int(length/2):]
        double_items = ''
        for item in compartment1:
            if item in compartment2 and item not in double_items:
                double_items = double_items + item
        items_sum = items_sum + priorities.find(double_items)
        print(f"{line_clean} - {len(line_clean)} - {compartment1} - {compartment2} - {double_items} - {priorities.find(double_items)} - {items_sum}")
    print(items_sum)
    