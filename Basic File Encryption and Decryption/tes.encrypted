def is_safe(board, row, col, n):
    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False

    return True


def solve_n_queens(board, row, n):
    # All queens are placed
    if row == n:
        print_board(board, n)
        return True

    solution_found = False

    # Try placing queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col

            if solve_n_queens(board, row + 1, n):
                solution_found = True

            board[row] = -1

    return solution_found


def print_board(board, n):
    print("\nSolution:")
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Input
n = int(input("Enter the value of N: "))

if n < 1:
    print("N must be greater than 0.")
else:
    board = [-1] * n

    if not solve_n_queens(board, 0, n):
        print("No solution exists.")