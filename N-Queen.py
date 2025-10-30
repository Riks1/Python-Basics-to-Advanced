def print_board(board, N):
    for i in range(N):
        for j in range(N):
            print('Q' if board[i][j] else '.', end=' ')
        print()
    print()


def is_safe(board, row, col, N):
    # Check this column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j]:
            return False

    return True


def solve_n_queens(board, row, N, solutions):
    # Base case: all queens placed
    if row == N:
        # Store a copy of current board configuration
        solutions.append([''.join('Q' if c else '.' for c in row) for row in board])
        return

    # Try placing a queen in each column
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens(board, row + 1, N, solutions)
            board[row][col] = 0  # backtrack


def n_queens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens(board, 0, N, solutions)

    print(f"Total solutions for {N} queens: {len(solutions)}\n")
    for sol in solutions:
        for row in sol:
            print(row)
        print()


# Run program
if __name__ == "__main__":
    N = int(input("Enter number of queens: "))
    n_queens(N)
