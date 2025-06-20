def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

a = int(input())
print('YES' if is_symmetric([list(map(int, input().split())) for i in range(a)]) else 'NO')
