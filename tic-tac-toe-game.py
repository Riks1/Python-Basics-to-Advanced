# A complete, command-line based Tic Tac Toe game in Python.

# Global constant for the board
BOARD = [' ' for _ in range(9)] # A list of 9 strings, initially all spaces
CURRENT_PLAYER = "X"
GAME_RUNNING = True

def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.
    The board is represented as a list of 9 elements.
    """
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")

def get_player_input(board, player):
    """
    Prompts the current player for their move (1-9) and validates it.
    The move must be an integer between 1 and 9, and the corresponding
    spot on the board must be empty.
    """
    while True:
        try:
            move = int(input(f"Player '{player}', enter your move (1-9): "))
            
            # Check if move is within the valid range
            if 1 <= move <= 9:
                # Check if the chosen spot is empty
                # We subtract 1 because moves are 1-indexed, but our list is 0-indexed
                if board[move - 1] == ' ':
                    return move - 1 # Return the 0-indexed position
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(board, player):
    """
    Checks if the specified player has won the game.
    Returns True if the player has won, False otherwise.
    """
    # Define all possible winning combinations (rows, columns, diagonals)
    win_conditions = [
        # Rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Columns
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonals
        [0, 4, 8], [2, 4, 6]
    ]
    
    # Check each win condition
    for condition in win_conditions:
        if (board[condition[0]] == player and
            board[condition[1]] == player and
            board[condition[2]] == player):
            return True
    return False

def check_draw(board):
    """
    Checks if the game is a draw (i.e., all spots are filled).
    Returns True if it's a draw, False otherwise.
    Assumes check_win has already been called and no winner was found.
    """
    # If there are no empty spaces left, it's a draw
    return ' ' not in board

def switch_player():
    """
    Switches the current player from 'X' to 'O' or from 'O' to 'X'.
    """
    global CURRENT_PLAYER
    if CURRENT_PLAYER == "X":
        CURRENT_PLAYER = "O"
    else:
        CURRENT_PLAYER = "X"

def main_game():
    """
    The main game loop.
    """
    global GAME_RUNNING
    
    print("Welcome to Tic Tac Toe!")
    print_board(BOARD)

    while GAME_RUNNING:
        # 1. Get the current player's move
        move = get_player_input(BOARD, CURRENT_PLAYER)
        
        # 2. Update the board
        BOARD[move] = CURRENT_PLAYER
        
        # 3. Print the updated board
        print_board(BOARD)
        
        # 4. Check if the current player has won
        if check_win(BOARD, CURRENT_PLAYER):
            print(f"Congratulations! Player '{CURRENT_PLAYER}' wins!")
            GAME_RUNNING = False
        
        # 5. Check if the game is a draw
        elif check_draw(BOARD):
            print("It's a draw! Good game.")
            GAME_RUNNING = False
            
        # 6. If the game is not over, switch players
        else:
            switch_player()

# Start the game when the script is run
if __name__ == "__main__":
    main_game()
