n = int(input())

matrix = []

primary_d = 0
secondary_d = 0

for row in range(n):
    matrix.append([int(el) for el in input().split()])
    primary_d += matrix[row][row]

for row in range(len(matrix)):
    col = (len(matrix)) - row - 1
    secondary_d += matrix[row][col]

print(abs(primary_d - secondary_d))
