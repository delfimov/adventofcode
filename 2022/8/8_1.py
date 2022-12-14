trees = []

def get_score(trees, row_n, col_n):
    tree = trees[row_n][col_n]
    if row_n == 0 or col_n == 0 or row_n == len(trees)-1 or col_n == len(trees[row_n])-1:
        return 0
    
    score_top = 1
    score_bottom = 1
    score_left = 1
    score_right = 1

    i = col_n-1
    while i > 0 and trees[row_n][i] < tree:
        i -= 1
        score_left += 1
    
    i = col_n+1
    while i < len(trees[row_n])-1 and trees[row_n][i] < tree:
        i += 1
        score_right += 1
    
    i = row_n-1
    while i > 0 and trees[i][col_n] < tree:
        i -= 1
        score_top += 1

    i = row_n+1
    while i < len(trees)-1 and trees[i][col_n] < tree:
        i += 1
        score_bottom += 1

    return score_top * score_bottom * score_left * score_right

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
    max_score = 0
    for trees_row in trees:
        col = 0
        for tree in trees_row:
            score = get_score(trees, row, col)
            if score > max_score:
               max_score = score
            col += 1
        row += 1
    print(max_score)