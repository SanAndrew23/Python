def is_correct_by_row(matrix):
    for row in matrix:
        row = sorted(row)
        for j in range(1, len(row) + 1):
            if row[j - 1] != j:
                return False
    return True


def transpose(matrix):
    matrix = [row.copy() for row in matrix]
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix


def is_correct_by_column(matrix):
    matrix = transpose(matrix)
    return is_correct_by_row(matrix)


def is_correct_by_squares(matrix, a):
    for x in range(0, a ** 2, a):
        for y in range(0, a**2, a):
            set = []
            for i in range(x, a + x):
                for j in range(x, a + x):
                    set.append(matrix[i][j])
            set = sorted(set)
            for i in range(1, len(set) + 1):
                if set[i - 1] != i:
                    return False
    return True


a = int(input())
matrix = [list(map(int, input().split())) for i in range(a ** 2)]

if is_correct_by_row(matrix) and is_correct_by_column(matrix) and is_correct_by_squares(matrix, a):
    print('YES')
else:
    print('NO')
