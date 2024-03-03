b_line = '|'
h_line = '_______'

game_board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

def print_board(board):
    print(h_line)
    for row in board:
        print(b_line + b_line.join(row) + b_line)
        print(h_line)

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
     for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
     if [board[i][i] for i in range(3)].count(player) == 3:
        return True
    if [board[i][2 - i] for i in range(3)].count(player) == 3:
        return True
    return False

current_player = 'X'
while True:
    print_board(game_board)
    try:
        move = int(input(f"Куди ставити {current_player} ?"))
        if move < 1 or move > 9:
            print("Введіть число від 1 до 9.")
            continue
        for row in game_board:
            if str(move) in row:
                if row[row.index(str(move))] in ['X', 'O']:
                    print("Ця клітинка вже зайнята. Оберіть іншу.")
                    break
                else:
                    row[row.index(str(move))] = current_player
                    break
    except ValueError:
        print("Введіть ціле число.")
        continue

     if check_winner(game_board, current_player):
        print_board(game_board)
        print(f"{current_player} переміг!")
        break


    if all([cell in ['X', 'O'] for row in game_board for cell in row]):
        print_board(game_board)
        print("Нічия!")
        break

    current_player = 'O' if current_player == 'X' else 'X'
