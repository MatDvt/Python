def read_matrix(rows):
    matrix = []
    for row in range(rows):
        matrix.append([el for el in input().split()])
    return matrix


rows, cols = [int(el) for el in input().split()]

matrix = read_matrix(rows)
count_squares = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        # print(
        #     matrix[row][col], matrix[row][col + 1],
        #     matrix[row + 1][col], matrix[row + 1][col + 1]
        # )
        if matrix[row][col] == matrix[row][col + 1] and \
                matrix[row][col] == matrix[row + 1][col] \
                and matrix[row][col] == matrix[row + 1][col + 1]:
            count_squares += 1

if count_squares >= 0:
    print(count_squares)
else:
    print(f"No 2x2 squares of equal cells exist.")

