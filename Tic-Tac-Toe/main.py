def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("|---|---|---|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|---|---|---|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")

def check_win(board, player):
    """Checks if a player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return ' ' not in board

def computer_turn(board):
    """Computer's turn to make a move."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]

    for condition in win_conditions:
        line = [board[i] for i in condition]
        if line.count('O') == 2 and ' ' in line:
            empty_index = condition[line.index(' ')]
            board[empty_index] = 'O'
            return

    for condition in win_conditions:
        line = [board[i] for i in condition]
        if line.count('X') == 2 and ' ' in line:
            empty_index = condition[line.index(' ')]
            board[empty_index] = 'O'
            return

    empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
    if empty_cells:
        board[empty_cells[0]] = 'O'
    else:
        print("Error, no move available.")
        return

def player_turn(board):
    """Player's turn to make a move."""
    while True:
        try:
            position = int(input("Enter a number between 1-9: ")) - 1
            if 0 <= position < 9 and board[position] == ' ':
                board[position] = 'X'
                return
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    """Main game loop."""
    board = [' '] * 9
    game_over = False

    while not game_over:
        print_board(board)
        player_turn(board)
        if check_win(board, 'X'):
            print_board(board)
            print("You win!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            computer_turn(board)
            if check_win(board, 'O'):
                print_board(board)
                print("Computer wins!")
                game_over = True
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                game_over = True

if __name__ == "__main__":
    play_game()