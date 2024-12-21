x = int(input())

pos = 0
neg = 0
nul = 0

for i in range(x):
    ch = int(input())
    if ch > 0:
        pos += 1
    elif ch < 0:
        neg += 1
    else:
        nul += 1

print(f'Положительные: {pos: 5d}')
print(f'Отрицательные: {neg: 5d}')
print(f'Нулевые: {nul: 11d}')
