def decode(x):
    table = [32, 15, 48, 12, 58, 73, 21, 45, 81, 39]
    for i in range(10):
        if table[i] == x:
            return i
    return -1

n = int(input())
sign = 1
if n < 0:
    sign = -1
    n *= -1
x1 = n // 10000
x2 = n // 100 % 100
x3 = n % 100
print((decode(x1) * 100 + decode(x2) * 10 + decode(x3)) * sign)
