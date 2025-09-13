def print_matrix(matrix):
    for row in matrix:
        for e in row:
            print(f'{e:3d}', end='')
        print()


def multiplication_table(row, col):
    return [[i * j for j in range(col)] for i in range(row)]


def chess_gen(row, col):
    return [[(j + i + 1) % 2 for j in range(col)] for i in range(row)]


def Andrews_cross(size):
    return [[1 if i == j or j == size - i - 1 else 0 for j in range(size)] for i in range(size)]


def quadrants(size):
    return [[
        0 if i == j or j == size - 1 - i else 1 if j > i and j < size - i - 1 else 4 if j < i and j < size - i - 1 and i < size - 1 else 2 if j > i else 3
        for j in range(size)] for i in range(size)]


def nested_squares(row, col):
    return [[min(i, j, row - i - 1, col - j - 1) for j in range(col)] for i in range(row)]


def spiral(row, col):
    matrix = [[0 for j in range(col)] for i in range(row)]
    x = 0
    for i in range(min(col + 1, row + 1) // 2):
        for a in range(i, col - i - 1):
            matrix[i][a] = x
            x += 1

        for b in range(i, row - i):
            matrix[b][col - 1 - i] = x
            x += 1

        for c in range(row - i, i, -1):
            matrix[row - i - 1][c] = x
            x += 1

        for d in range(i, row - i - 1):
            matrix[row - 1 - d][i] = x
            x += 1
    return matrix


print_matrix(spiral(3, 5))
