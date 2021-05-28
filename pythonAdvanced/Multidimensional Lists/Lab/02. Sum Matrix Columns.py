rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(" ")])

for col in range(cols):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][col]
    print(current_sum)
