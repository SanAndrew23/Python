a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    h = max(a, b, c)
    k1 = min(a, b, c)
    k2 = a + b + c - h - k1
    if h**2 == k1**2 + k2**2:
        print('Прямоугольный')
    elif h**2 < k1**2 + k2** 2:
        print('Остроугольный')
    elif h**2 > k1**2 + k2**2:
        print('Тупоугольный')
else:
    print('Не существует')