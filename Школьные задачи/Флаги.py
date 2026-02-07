n = int(input())
s_1 = '+___ ' * n
s_2 = ''
for i in range(1, n + 1):
    s_2 += f'|{i} / '
s_3 = '|__\\ ' * n
s_4 = '|    ' * n

print(s_1, s_2, s_3, s_4, sep='\n')
