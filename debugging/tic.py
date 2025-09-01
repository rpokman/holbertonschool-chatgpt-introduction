#!/usr/bin/python3
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return row[0]
    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid coordinates. Use 0, 1, or 2.")
            continue
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue
        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player " + winner + " wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"

tic_tac_toe()
