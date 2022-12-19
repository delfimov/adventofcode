with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    count = 0
    total = 0
    for line in lines:
        line_clean = line.strip()
        parts = line_clean.split(',')
        parts1 = parts[0].split('-')
        parts2 = parts[1].split('-')
        total += 1
        if (int(parts1[0]) >= int(parts2[0]) and int(parts1[1]) <= int(parts2[1])) or (int(parts2[0]) >= int(parts1[0]) and int(parts2[1]) <= int(parts1[1])):
            count += 1
    print(count)