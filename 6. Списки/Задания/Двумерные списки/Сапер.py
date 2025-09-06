def create_map(matrix, i, j):
    n, m = len(matrix), len(matrix[0])
    matrix[i][j] = '*'
    if i + 1 <= n - 1 and matrix[i + 1][j] != '*':
        matrix[i + 1][j] += 1
    if j + 1 <= m - 1 and matrix[i][j + 1] != '*':
        matrix[i][j + 1] += 1
    if i - 1 >= 0 and matrix[i - 1][j] != '*':
        matrix[i - 1][j] += 1
    if j - 1 >= 0 and matrix[i][j - 1] != '*':
        matrix[i][j - 1] += 1
    if j + 1 <= m - 1 and i - 1 >= 0 and matrix[i - 1][j + 1] != '*':
        matrix[i - 1][j + 1] += 1
    if j - 1 >= 0 and i - 1 >= 0 and matrix[i - 1][j - 1] != '*':
        matrix[i - 1][j - 1] += 1
    if j - 1 >= 0 and i + 1 <= n - 1 and matrix[i + 1][j - 1] != '*':
        matrix[i + 1][j - 1] += 1
    if j + 1 <= m - 1 and i + 1 <= n - 1 and matrix[i + 1][j + 1] != '*':
        matrix[i + 1][j + 1] += 1


def print_matrix(matrix):
    for row in matrix:
        for e in row:
            print(e if e != 0 else '.', end='')
        print()


n, m, k = map(int, input().split())
matrix = [[0] * m for i in range(n)]

for x in range(k):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    create_map(matrix, i, j)

print_matrix(matrix)
