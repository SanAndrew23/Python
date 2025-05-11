s = input().split(' ')
x = len(s)
a = 0
print(' ', end ='')
while x != 0:
    if len(s[a]) > 2:
        print(f'{s[a][0].lower()}{s[a][1].upper()}{s[a][2:].lower()}', end = ' ')
    else:
        print(s[a].lower(), end = ' ')
    x -= 1
    a += 1