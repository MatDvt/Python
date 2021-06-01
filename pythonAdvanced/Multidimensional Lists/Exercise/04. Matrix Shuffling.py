def read_matrix(rows):
    matrix = []
    for row in range(rows):
        matrix.append([int(el) for el in input().split()])
    return matrix


rows, cols = [int(el) for el in input().split()]
matrix = read_matrix(rows)

command, row1, col1, row2, col2 = input().split()
# row1, col1, row2, col2 = int(row1), int(col1), int(row2), int(col2)

while not command == "END":
    row1, col1, row2, col2 = int(row1), int(col1), int(row2), int(col2)

    if row1 in range(rows) and row2 in range(rows) and col1 in range(cols) and col2 in range(cols):

        temp_value = matrix[row1][col1]
        matrix[row1][col1] = matrix[row2][col2]
        matrix[row2][col2] = temp_value
        print([matrix])
    else:
        print(f"Invalid Input")
    command, row1, col1, row2, col2 = input().split()

print(matrix)
