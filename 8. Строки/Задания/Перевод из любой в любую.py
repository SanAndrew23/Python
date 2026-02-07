def to_dec(num, base):
    sum = 0
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = num[::-1]
    for i in range(len(num)):
        sum += (alph.find(num[i]) * (base ** i))

    return sum


def from_dec(num, base):
    res = ''
    alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while num > 0:
        res = alph[num % base] + res
        num //= base
    return res


num = input()
k, m = map(int, input().split())
print(from_dec(to_dec(num, k), m))