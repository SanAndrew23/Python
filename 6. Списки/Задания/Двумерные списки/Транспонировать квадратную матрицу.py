def transpose(matrix):
    matrix = [row.copy() for row in matrix]
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for e in row:
            print(f'{e:<3d}', end='')
        print()
    print()


a = int(input())
matr = [list(map(int, input().split())) for i in range(a)]
print_matrix(transpose(matr))