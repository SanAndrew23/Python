# Дано целое число N. Выбросить из его записи цифры 0 и 5, сохранив прежний порядок остальных цифр.
num = int(input())
new_num = 0

i = 1
while num > 0:
    digit = num % 10
    if digit != 0 and digit != 5:
        new_num += digit * i
        i *= 10
    num //= 10
print(new_num)
