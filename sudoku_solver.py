def is_valid(board, row, col, num):
    # Check if the number is not in the given row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is not in the given column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is not in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    # Find an empty cell in the board
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # Solution found

    row, col = empty_cell

    # Try placing numbers 1-9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            # Recursively try to solve the board with the current number placed
            if solve_sudoku(board):
                return True

            # Backtrack if placing the current number didn't lead to a solution
            board[row][col] = 0

    return False  # No valid number found, backtrack

def find_empty(board):
    # Find an empty cell in the board (represented by 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    # Print the board in a formatted way
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


"""
# Example board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the original board
print("Original board:")
print_board(board)

# Solve the Sudoku puzzle
if solve_sudoku(board):
    print("\nSolved board:")
    print_board(board)
else:
    print("No solution exists.")
"""