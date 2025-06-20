def transpose(matrix):
    for i in range(a):
        for j in range(b):
            return [(j for i in range(b)) for i in range(a)]


def print_matrix(matrix):
    for row in matrix:
        for e in row:
            print(f'{e:3d}', end='')
        print()


a, b = map(int, input().split())
print(transpose(list[(int(input()) for i in range(a))] for j in range(b)))