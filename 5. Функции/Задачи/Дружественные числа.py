def is_friendly_numbers(a, b):
    sum_a = 0
    sum_b = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a += i
    for i in range(1, b):
        if b % i == 0:
            sum_b += i
    return sum_a == b and sum_b == a

a, b = map(int, input().split())
x = 0
for i in range(a, b):
    for j in range(i + 1, b):
        if is_friendly_numbers(i, j):
            print(f'({i} {j})', end = '')
            x += 1
if x == 0:
    print('0')