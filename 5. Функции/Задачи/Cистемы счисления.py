def translate(num, system):
    alph = '0123456789ABCDEFGHI'
    if num != 0:
        translate(num // system, system)
        print(alph[num % system], end='')


num, system = map(int, input().split())
translate(num, system)
