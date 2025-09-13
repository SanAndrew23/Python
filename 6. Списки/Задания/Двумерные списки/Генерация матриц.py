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
    for i in range(min(row, col) // 2 + (min(row, col) % 2)):
        for a in range(i, col - i):
            matrix[i][a] = x
            x += 1

        for b in range(i + 1, row - i):
            matrix[b][col - 1 - i] = x
            x += 1

        if x < row * col:
            for c in range(col - i - 1, i, -1):
                matrix[row - i - 1][c - 1] = x
                x += 1
        if x < row * col:
            for d in range(row - i - 1, i + 1, -1):
                matrix[d - 1][i] = x
                x += 1
    '''top, bottom, left, right = 0, row, 0, col
    while top < bottom and left < right:
        # Заполнение верхней строки слева направо
        for i in range(left, right):
            matrix[top][i] = x
            x += 1
        top += 1
        # Заполнение правого столбца сверху вниз
        for i in range(top, bottom):
            matrix[i][right - 1] = x
            x += 1
        right -= 1
        if top < bottom:
            # Заполнение нижней строки справа налево
            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = x
                x += 1
            bottom -= 1
        if left < right:
            # Заполнение левого столбца снизу вверх
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = x
                x += 1
            left += 1'''
    return matrix


print_matrix(spiral(2, 7))
