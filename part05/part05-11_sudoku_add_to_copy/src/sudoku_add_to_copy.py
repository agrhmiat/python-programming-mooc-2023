# Write your solution here

def print_sudoku(sudoku: list) -> None:
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            square = sudoku[i][j]
            if square > 0:
                print(f"{square} ", end="")
            else:
                print("_ ", end="")
            if (j+1) % 3 == 0:
                print(" ", end="")
        if (i+1) % 3 == 0:
            print()
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    sudoku_copy = []
    for i in range(len(sudoku)):
        row = []
        for j in range(len(sudoku[i])):
            row.append(sudoku[i][j])
        sudoku_copy.append(row)
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
