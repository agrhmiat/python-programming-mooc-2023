# write your solution here

def read_matrix() -> list:
    with open("matrix.txt") as new_file:
        matrix = []
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            row = []
            for part in parts:
                row.append(int(part))
            matrix.append(row)
    return matrix

def matrix_sum():
    row_sum = row_sums()
    total = 0
    for row in row_sum:
        total += row
    return total

def matrix_max():
    matrix = read_matrix()
    max_number = matrix[0][0]
    for row in matrix:
        for num in row:
            if num > max_number:
                max_number = num
    return max_number

def row_sums():
    matrix = read_matrix()
    row_sum = []
    for row in matrix:
        total = 0
        for num in row:
            total += num
        row_sum.append(total)
    return row_sum

if __name__ == "__main__":
    print(row_sums())
    print(matrix_sum())
    print(matrix_max())
