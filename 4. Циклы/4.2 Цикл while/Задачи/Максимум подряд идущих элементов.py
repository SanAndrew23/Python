a = int(input())

kol = 0
kol_1 = 0
maxim = 0

while a != 0:
    a = int(input())
    if a == maxim:
        kol = kol+1
    elif a > maxim:
        maxim = a
        kol_1 += 1
    if kol < kol_1:
        maxim = kol_1
    kol = 0
print(maxim)
