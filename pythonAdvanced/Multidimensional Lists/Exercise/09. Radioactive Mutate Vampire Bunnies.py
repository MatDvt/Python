def read_square_matrix():
    matrix = []
    rows_count = int(input())

    for row in range(rows_count):
        matrix.append([int(el) for el in input().split()])

    return matrix


def get_bombs_coordinates():
    raw_coordinates = input().split()
    bombs_coordinates = []
    for i in range(len(raw_coordinates)):
        current_coord = tuple(map(int, raw_coordinates[i].split(',')))
        bombs_coordinates.append(current_coord)

    return bombs_coordinates


def detonate_bomb(bomb_coordinates, matrix):
    row, col = bomb_coordinates
    bomb_value = matrix[row][col]
    cells_to_reduce = [(row, col), (row-1, col-1), (row-1, col), (row-1, col+1),
                       (row, col+1), (row+1, col+1), (row+1, col),
                       (row+1, col-1), (row, col-1)]
    for cell in cells_to_reduce:
        cell_row, cell_col = cell
        if 0 <= cell_row < len(matrix) and 0 <= cell_col < len(matrix):
            if not matrix[cell_row][cell_col] <= 0:
                matrix[cell_row][cell_col] -= bomb_value


def find_alive_cells(matrix):
    alive_cells_positions = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if not matrix[row][col] <= 0:
                alive_cells_positions.append((row, col))

    return alive_cells_positions


def get_alive_cells_sum(matrix):
    alive_cells_sum = 0
    for cell in find_alive_cells(matrix):
        cell_row, cell_col = cell
        alive_cells_sum += matrix[cell_row][cell_col]

    return f"Sum: {alive_cells_sum}"


def main():
    matrix = read_square_matrix()

    all_bombs = get_bombs_coordinates()

    for i in range(len(all_bombs)):
        bomb_coordinates = all_bombs[i]
        detonate_bomb(bomb_coordinates, matrix)

    print(f"Alive cells: {len(find_alive_cells(matrix))}")
    print(get_alive_cells_sum(matrix))

    for row in range(len(matrix)):
        print(*matrix[row], sep=' ')


main()

# rows, cols = [int(x) for x in input().split()]
#
#
# def read_matrix(rows):
#     matrix = []
#     for _ in range(rows):
#         matrix.append(list(input()))
#     return matrix
#
#
# def find_player(matrix):
#     for row in range(len(matrix)):
#         for col in range(len(matrix[0])):
#             if matrix[row][col] == 'P':
#                 return [row, col]
#
#
# def is_move_valid(row, col):
#     return 0 <= row < rows and 0 <= col < cols
#
#
# def player_move(row, col, direction):
#     if direction == 'U':
#         potential_row = row - 1
#         potential_col = col
#     elif direction == 'R':
#         potential_col = col + 1
#         potential_row = row
#     elif direction == 'D':
#         potential_row = row + 1
#         potential_col = col
#     elif direction == 'L':
#         potential_col = col - 1
#         potential_row = row
#
#     if is_move_valid(potential_row, potential_col):
#         matrix[row][col] = '.'
#         if matrix[potential_row][potential_col] == 'B':
#             return ('dead', potential_row, potential_col)
#         matrix[potential_row][potential_col] = 'P'
#         return potential_row, potential_col
#     matrix[row][col] = '.'
#     return 'won', row, col
#
#
# def get_bunnies_indexes(matrix):
#     bunnies = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 'B':
#                 bunnies.append([i, j])
#
#     return bunnies
#
#
# def mutate_bunny(matrix, row, col, is_dead):
#     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     for position in directions:
#         potential_row = row + position[0]
#         potential_col = col + position[1]
#         if is_move_valid(potential_row, potential_col):
#             if matrix[potential_row][potential_col] == 'P':
#                 is_dead = True
#                 dead_row, dead_col = potential_row, potential_col
#             matrix[potential_row][potential_col] = 'B'
#     if is_dead:
#         return is_dead, dead_row, dead_col
#
#
# def bunnies_mutate(matrix, is_dead):
#     result = None
#     bunnies = get_bunnies_indexes(matrix)
#     for bunny in bunnies:
#         res = mutate_bunny(matrix, bunny[0], bunny[1], is_dead)
#         if res:
#             result = res
#     return result
#
#
# matrix = read_matrix(rows)
# player_position = find_player(matrix)
# commands = list(input())
# is_dead = False
#
# for direction in commands:
#     res = player_move(player_position[0], player_position[1], direction)
#
#     res_1 = bunnies_mutate(matrix, is_dead)
#     if res_1:
#         is_dead, row, col = res_1
#
#     if res[0] == 'dead':
#         for row in matrix:
#             print(''.join(row))
#         print(f'dead: {res[1]} {res[2]}')
#         break
#     elif res[0] == 'won':
#         for row in matrix:
#             print(''.join(row))
#         print(f'won: {res[1]} {res[2]}')
#         break
#     else:
#         player_position[0], player_position[1] = res[0], res[1]
#
#     if is_dead:
#         for _ in matrix:
#             print(''.join(_))
#         print(f'dead: {row} {col}')
#         break