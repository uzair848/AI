def print_board(board):
    """Prints the board using dotted/dashed lines."""
    print("\n  0   1   2")
    for i in range(3):
        
        row_cells = [cell if cell != -1 else " " for cell in board[i]]
        print(f"{i} {row_cells[0]} | {row_cells[1]} | {row_cells[2]}")
        if i < 2:
            print("  --+---+--")
    print()


def check_win(board, symbol):
   
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False


def play_game():
    board = [[-1 for _ in range(3)] for _ in range(3)]
    counter = 0
    p = 0

    print("--- Tic Tac Toe ---")

    while counter < 9:
        print_board(board)

        symbol = "X" if p == 0 else "O"
        print(f"Player {p}'s turn ({symbol}):")

        

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == -1:
               
                board[row][col] = symbol
                counter += 1
             

                
                if check_win(board, symbol):
                    print_board(board)
                    return f"Player {p} won!"

               
                p = 1 - p
            else:
                print("Cell is already occupied! Try again.\n")
        else:
            print("Out of bounds! Row and column must be 0, 1, or 2.\n")
        

    print_board(board)
    return "Draw"



result = play_game()
print("\nGame Result:", result) 
