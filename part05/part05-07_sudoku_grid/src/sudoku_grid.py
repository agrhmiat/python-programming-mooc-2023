# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    nums = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            num = sudoku[i][j]
            if num > 0 and num in nums:
                return False
            nums.append(num)
    return True

def column_correct(sudoku: list, column_no: int) -> bool:
    nums = []
    for row in sudoku:
        num = row[column_no]
        if num > 0 and num in nums:
            return False
        nums.append(num)
    return True

def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    nums = []
    for num in row:
        if num > 0 and num in nums:
            return False
        nums.append(num)
    return True

def sudoku_grid_correct(sudoku: list) -> bool:
    for i in range(len(sudoku)):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False
    for i in range(len(sudoku)):
        if i%3 == 0:
            for j in range(len(sudoku[i])):
                if j%3 == 0:
                    if not block_correct(sudoku, i, j):
                        return False
    return True

if __name__ == "__main__":
    sudoku1 = [
      [9, 0, 0, 0, 8, 0, 3, 0, 0],
      [2, 0, 0, 2, 5, 0, 7, 0, 0],
      [0, 2, 0, 3, 0, 0, 0, 0, 4],
      [2, 9, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 7, 3, 0, 5, 6, 0],
      [7, 0, 5, 0, 6, 0, 4, 0, 0],
      [0, 0, 7, 8, 0, 3, 9, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 3],
      [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
      [2, 6, 7, 8, 3, 9, 5, 0, 4],
      [9, 0, 3, 5, 1, 0, 6, 0, 0],
      [0, 5, 1, 6, 0, 0, 8, 3, 9],
      [5, 1, 9, 0, 4, 6, 3, 2, 8],
      [8, 0, 2, 1, 0, 5, 7, 0, 6],
      [6, 7, 4, 3, 2, 0, 0, 0, 5],
      [0, 0, 0, 4, 5, 7, 2, 6, 3],
      [3, 2, 0, 0, 8, 0, 0, 5, 7],
      [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
