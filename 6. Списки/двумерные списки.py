def print_matrix(matrix):
    for row in matrix:
        for e in row:
            print(f'{e:3d}', end='')
        print()


# ПРАВИЛЬНАЯ Генерация пустого двумерного списка
matrix1 = [[0] * 10 for i in range(10)]
matrix1 = [[i * j for j in range(10)] for i in range(10)]

# НЕПРАВИЛЬНАЯ (Создаются копии строк списка и меняются одновременно)
matrix2 = [[0] * 10] * 10

matrix1[0][0] = 100
matrix2[0][0] = 100

print_matrix(matrix1)
print_matrix(matrix2)