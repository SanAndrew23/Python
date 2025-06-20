def Transpose(matrix, a):
    for i in range(a):
        for j in range(a):
            matrix[i][j] = matrix[j][i]
    return matrix
a = int(input())
print(Transpose([list(map(int, input().split())) for i in range(a)], a))