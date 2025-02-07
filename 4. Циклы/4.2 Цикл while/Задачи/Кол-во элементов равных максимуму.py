a = int(input())

maxim = a
kol = 1

while a != 0:
    a = int(input())
    if a > maxim:
        maxim = a
        kol = 1
    elif a == maxim:
        kol += 1
print(kol)