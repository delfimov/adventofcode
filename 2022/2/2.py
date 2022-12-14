opponent = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
}
me = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
}
me2 = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}
draws = {
    'Rock': {'points': 1, 'lose': 'Scissors', 'win': 'Paper'},
    'Paper': {'points': 2, 'lose': 'Rock', 'win': 'Scissors'},
    'Scissors': {'points': 3, 'lose': 'Paper', 'win': 'Rock'},
}

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    my_points = 0
    opponent_points = 0
    my_points2 = 0
    opponent_points2 = 0
    for line in lines:
        draw = line.strip().split(' ')
        opponent_move = opponent[draw[0]]
        my_move = me[draw[1]]
        if me2[draw[1]] == 'draw':
            my_move2 = opponent_move
        else:
            my_move2 = draws[opponent_move][me2[draw[1]]]

        if opponent_move == my_move:
            my_points += 3
            opponent_points += 3
        elif draws[my_move]['lose'] == opponent_move:
            my_points += 6
        else:
            opponent_points += 6

        if opponent_move == my_move2:
            my_points2 += 3
            opponent_points2 += 3
        elif draws[my_move2]['lose'] == opponent_move:
            my_points2 += 6
        else:
            opponent_points2 += 6

        my_points += draws[my_move]['points']
        opponent_points += draws[opponent_move]['points']

        my_points2 += draws[my_move2]['points']
        opponent_points2 += draws[opponent_move]['points']

    print(f"My points: {my_points}")
    print(f"Opponent points: {opponent_points}")
    print(f"My points 2: {my_points2}")
    print(f"Opponent points 2: {opponent_points2}")
