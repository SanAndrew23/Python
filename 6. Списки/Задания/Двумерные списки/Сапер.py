def create_map(matrix, n, m, i, j):
    matrix[i][j] = '*'
    if i + 1 <= n - 1:
        matrix[i + 1][j] += 1
    if j + 1 <= m - 1:
        matrix[i][j + 1] += 1
    if i - 1 >= 0:
        matrix[i - 1][j] += 1
    if j - 1 >= 0:
        matrix[i][j - 1] += 1
    if j + 1 <= m - 1 and i - 1 >= 0:
        matrix[i - 1][j + 1] += 1
    if j - 1 >= 0 and i - 1 >= 0:
        matrix[i - 1][j - 1] += 1
    if j - 1 >= 0 and i + 1 <= n - 1:
        matrix[i + 1][j - 1] += 1
    if j + 1 <= m - 1 and i + 1 <= n - 1:
        matrix[i + 1][j + 1] += 1
        return matrix

def make_points(matrix, n, m):
    lst = ['*', '1', '2', '3', '4', '5', '6', '7', '8']
    for i in range(n):
        for j in range(m):
            if matrix[i][j] not in lst:
                matrix[i][j] = '.'


n, m, k = map(int, input().split())
matrix = [[0] * n for i in range(m)]

for x in range(k):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    create_map(matrix, n, m, i, j)

make_points(matrix, n, m)

print(matrix)
