def is_correct(matrix):
    for i in range(a**2):
        for j in range(a**2):
            if matrix[i] == matrix[j]:
                return False
    return True

a = int(input())
print(is_correct([list(map(int, input().split())) for i in range(a**2)]))