a = int(input())

kol = 1
kol_1 = 1
maxim = a
maxim_2 = 1

while a != 0:
    a = int(input())
    if a == maxim:
        kol +=1
    elif a < maxim:
        kol_1 = 1
        maxim_2 = a
    elif a == maxim_2:
        kol_1 += 1
if kol_1 > kol:
    kol = kol_1
print(kol)