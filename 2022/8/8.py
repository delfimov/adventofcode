trees = []

def is_visible(trees, row_n, col_n):
    tree = trees[row_n][col_n]
    row_count = 0
    is_visible_top = True
    is_visible_bottom = True
    is_visible_left = True
    is_visible_right = True
    for row in trees:
        if row_count < row_n and tree <= row[col_n]:
            is_visible_top = False
        if row_count > row_n and tree <= row[col_n]:
            is_visible_bottom = False
        row_count += 1
    col_count = 0
    for tree_in_col in trees[row_n]:
        if col_count < col_n and tree <= tree_in_col:
            is_visible_left = False
        if col_count > col_n and tree <= tree_in_col:
            is_visible_right = False
        col_count += 1
    return is_visible_top or is_visible_bottom or is_visible_left or is_visible_right

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        trees_row = []
        for tree in line.strip():
            trees_row.append(int(tree)) 
        trees.append(trees_row)
    rows = len(trees)
    cols = len(trees[0])
    row = 0
    visible = 0
    for trees_row in trees:
        col = 0
        for tree in trees_row:
            if col == 0 or row == 0 or col == cols-1 or row == rows-1:
                visible += 1
            elif is_visible(trees, row, col):
                visible += 1
            col += 1
        row += 1
    print(visible)