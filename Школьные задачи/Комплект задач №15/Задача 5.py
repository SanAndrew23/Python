import math

x = int(input())
items = list(map(float, input().split()))

if x == 1:
    if len(items) != 2:
        print('Ошибка ввода')
    else:
        print(f'{items[0] * items[1]:.2f}')

elif x == 2:
    if len(items) != 3:
        print('Ошибка ввода')
    else:
        p_tr = 0.5 * (items[0] + items[1] + items[2])
        print(f'{((p_tr * (p_tr - items[0]) * (p_tr - items[1]) * (p_tr - items[2])) ** 0.5):.2f}')
elif x == 3:
    if len(items) != 1:
        print('Ошибка ввода')
    else:
        print(f'{((items[0] / 2) ** 2 * math.pi):.2f}')