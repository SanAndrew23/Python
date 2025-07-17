def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    transposed_matrix = [[0] * row for i in range(col)]
    for i in range(row):
        for j in range(col):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

def print_matrix(matrix):
    for row in matrix:
        for e in row:
            print(f'{e:3d}', end='\n')
        print()


a, b = map(int, input().split())
matrix = [list(map(int, input().split())) for j in range(b)]
print(transpose(matrix))