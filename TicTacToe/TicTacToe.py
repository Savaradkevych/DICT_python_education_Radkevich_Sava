# tictactoe.py

def print_board(board):
    print("---------")
    for row in board:
        print(f"| {' '.join(row)} |")
    print("---------")

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def update_board(board, cells):
    index = 0
    for i in range(3):
        for j in range(3):
            board[i][j] = cells[index]
            index += 1

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return f"{board[i][0]} wins"
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return f"{board[0][i]} wins"

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return f"{board[0][0]} wins"
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return f"{board[0][2]} wins"

    return None

def check_game_state(board):
    winner = check_winner(board)
    if winner:
        return winner

    if any(' ' in row for row in board):
        return "Game not finished"

    return "Draw"

def make_move(board, symbol, row, col):
    if board[row - 1][col - 1] == ' ':
        board[row - 1][col - 1] = symbol
        return True
    else:
        print("This cell is occupied! Choose another one!")
        return False

def is_valid_input(user_input):
    try:
        row, col = map(int, user_input.split())
        if 1 <= row <= 3 and 1 <= col <= 3:
            return True, row, col
        else:
            print("Coordinates should be from 1 to 3!")
            return False, None, None
    except ValueError:
        print("You should enter numbers!")
        return False, None, None

# Початок гри
board = initialize_board()
print_board(board)

current_player = 'X'

while True:
    while True:
        user_input = input(f"Enter the coordinates for {current_player} (row column): ")
        valid_input, row, col = is_valid_input(user_input)

        if valid_input:
            if make_move(board, current_player, row, col):
                break

    game_state = check_game_state(board)
    print_board(board)
    print(game_state)

    if game_state in ["X wins", "O wins", "Draw"]:
        break

    # Смена игрока
    current_player = 'O' if current_player == 'X' else 'X'
