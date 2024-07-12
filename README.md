```markdown
# Sudoku Solver

This is a Python implementation of a Sudoku solver using the backtracking algorithm. The solver reads a Sudoku puzzle, solves it, and prints the solution.

## How It Works

The solver uses a recursive backtracking algorithm to fill in the empty cells in the Sudoku puzzle. It tries to place numbers 1-9 in each empty cell and checks if the placement is valid according to Sudoku rules. If a placement is valid, it moves on to the next empty cell. If not, it backtracks and tries the next number.

## Functions

### `is_valid(board, row, col, num)`
Checks if placing `num` in the given `row` and `col` of the `board` is valid according to Sudoku rules.

- **Parameters:**
  - `board` (list): The current state of the Sudoku board.
  - `row` (int): The row index of the cell.
  - `col` (int): The column index of the cell.
  - `num` (int): The number to be placed in the cell.

- **Returns:**
  - `bool`: True if the placement is valid, False otherwise.

### `solve_sudoku(board)`
Recursively solves the Sudoku puzzle using backtracking.

- **Parameters:**
  - `board` (list): The current state of the Sudoku board.

- **Returns:**
  - `bool`: True if the puzzle is solved, False if no solution exists.

### `find_empty(board)`
Finds an empty cell in the Sudoku board (represented by 0).

- **Parameters:**
  - `board` (list): The current state of the Sudoku board.

- **Returns:**
  - `tuple`: The row and column index of the empty cell, or None if no empty cells are found.

### `print_board(board)`
Prints the Sudoku board in a formatted way.

- **Parameters:**
  - `board` (list): The current state of the Sudoku board.

## Example Usage

Here is an example of how to use the Sudoku solver:

```python
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
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sudoku-solver.git
```

2. Navigate to the project directory:
```bash
cd sudoku-solver
```

3. Run the solver script:
```bash
python sudoku_solver.py
```

## License

This project is licensed under the MIT License.
```
