def is_valid(board, row, col, n):
    # Check for conflicts with queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for conflicts with queens in the upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for conflicts with queens in the upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # If there are no conflicts, the placement is valid
    return True


def solve_n_queens(board, row, n):
    # Base case: if all queens have been placed, return True
    if row == n:
        return True

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0

    # If no queen can be placed in the current row, backtrack
    return False


def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def n_queens():
    n = int(input("Enter the number of queens: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0, n):
        print_board(board, n)
    else:
        print("No solution found for", n, "queens.")


if __name__ == "__main__":
    n_queens()
