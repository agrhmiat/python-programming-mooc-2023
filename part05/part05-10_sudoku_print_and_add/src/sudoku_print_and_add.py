# Write your solution here

def add_number(sudoku: list, row_no: int, column_no: int, number: int) -> None:
    sudoku[row_no][column_no] = number

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

if __name__ == "__main__":
    s = [
      [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
      [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
      [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
      [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
      [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
      [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
      [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
      [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
      [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]
    print_sudoku(s)
    print()
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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
