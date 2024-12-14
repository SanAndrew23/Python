x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())

if x == x1 or y == y1 or x1 - 1 == x or x1 + 1 == x or y1 - 1 == y or y1 + 1 == y:
    print('YES')
else:
    print('NO')