def to_dec(num, base):
    sum = 0
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = num[::-1]
    for i in range(len(num)):
        sum += (alph.find(num[i]) * (base ** i))

    return sum


def from_dec(num, base):
    summ = ''
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while num % base != 0:
        summ += alph[num % base]
        num //= base

    summ = summ[::-1]
    return summ


num = input()
k, m = map(int, input().split())
print(from_dec(to_dec(num, k), m))