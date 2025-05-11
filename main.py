num = abs(int(input()))
i = 0
mul = 1
summa = 0
while num != 0:
    if num % 10 % 3 == 0 and num % 10 != 0:
        summa += (num % 10)
        mul *= (num % 10)
    if num % 10 == 0:
        i += 1
    num //= 10
if summa != 0:
    print(f'{mul / summa:.2f}')
elif summa != 0 and i > 0:
    print(f'{mul / summa:.2f}')
elif summa == 0 and i > 0:
    print('0')
else:
    print('NO')
