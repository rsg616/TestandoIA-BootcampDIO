def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row, col = map(int, input(f"Jogador {player}, insira linha e coluna (0-2): ").split())

        if board[row][col] != " ":
            print("Posição ocupada, tente novamente.")
            continue

        board[row][col] = player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Jogador {winner} venceu!")
            break
        elif is_full(board):
            print_board(board)
            print("Empate!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()