def read_matrix(rows):
    matrix = []
    for row in range(rows):
        matrix.append([int(el) for el in input().split()])
    return matrix


rows, cols = [int(el) for el in input().split()]

matrix = read_matrix(rows)

max_sum = None
max_start_row, max_start_col = 0, 0

for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = sum([
            matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2],
        ])
        if max_sum is None or max_sum < current_sum:
            max_sum = current_sum
            max_start_row, max_start_col = i, j
print(f"Sum = {max_sum}")
for i in range(3):
    for j in range(3):
        print(matrix[max_start_row + i][max_start_col + j], end=" ")
    print()