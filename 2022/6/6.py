def get_pos(line: str) -> int:
    marker = ''
    position = 0
    for char in line:
        position += 1
        if char in marker:
            marker = marker[int(marker.find(char)+1):]
        marker += char
        if len(marker) == 4:
            break
    return position

with open('input.txt', 'r', encoding="utf-8") as f:
    print(get_pos(f.readline()))
