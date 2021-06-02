def read_matrix(rows):
    matrix = []
    for row in range(rows):
        matrix.append([el for el in input().split()])
    return matrix


def valid_command(data):
    if int(data[1]) in range(rows) and \
            int(data[3]) in range(rows) and \
            int(data[2]) in range(cols) and \
            int(data[4]) in range(cols) and \
            data[0] == "swap" and len(data) == 5:
        return True


def swap_elements(matrix):
    temp_value = matrix[row1][col1]
    matrix[row1][col1] = matrix[row2][col2]
    matrix[row2][col2] = temp_value


rows, cols = [int(el) for el in input().split()]
matrix = read_matrix(rows)

data = [el for el in input().split()]

while not data[0] == "END":
    if valid_command(data):
        command, row1, col1, row2, col2 = data[0], int(data[1]), int(data[2]), int(data[3]), int(data[4])
        swap_elements(matrix)
        print('\n'.join([" ".join(m) for m in matrix]))
    else:
        print(f"Invalid input!")
    data = input().split()


# alternative one

# rows, columns = list(map(int, input().split(" ")))
#
# matrix = [input().split() for _ in range(rows)]
#
# line = input()
# while not line == "END":
#     try:
#         swap, row1, col1, row2, col2 = line.split()
#         row1 = int(row1)
#         col1 = int(col1)
#         row2 = int(row2)
#         col2 = int(col2)
#         if swap == "swap" and row1 in range(len(matrix)) and col1 in range(len(matrix)) and row2 in range(len(matrix)) and col2 in range(len(matrix)):
#             matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#             print('\n'.join([" ".join(m) for m in matrix]))
#         else:
#             print("Invalid input!")
#     except ValueError:
#         print("Invalid input!")
#
#     line = input()