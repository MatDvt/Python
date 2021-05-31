n = int(input())

matrix = []

for row in range(n):
    matrix.append(list(input()))  # split to chars instead of using split which results in a string

symbol = input()
position = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            position = (row, col)
            break  # we need the first occurrence
    if position:
        break

# print(position if position else f'{symbol} does not occur in the matrix') # shortcut for printing it on one line

if position:
    print(position)
else:
    print(f'{symbol} does not occur in the matrix')
