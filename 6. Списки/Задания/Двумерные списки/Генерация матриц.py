def print_matrix(matrix):
    for row in matrix:
        for e in row:
            print(f'{e:3d}', end='')
        print()


def multiplication_table(row, col):
    return [[i * j for j in range(col)] for i in range(row)]


def chess_gen(row, col):
    return [[(j + i + 1) % 2 for j in range(col)] for i in range(row)]


def Andrews_cross(row, col):
    return [[1 if i == j or j == col - i - 1 else 0 for j in range(col)] for i in range(col)]


def quadrants(row, col):
    return [[for j in range(col)] for i in range(col)]


def nested_squares(row, col):
    return [[ for j in range(col)] for i in range(col)]


def spiral(row, col):
    return [[ for j in range(col)] for i in range(col)]


print_matrix(spiral(7, 7))
