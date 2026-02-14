d = dict() #name: cash
do_commands = ['DEPOSIT', 'WITHDRAW']
res = []
for i in range(int(input())):
    st = input().split()
    if st[0] in do_commands:
        name = st[1]
        if name not in d:
            d[name] = 0
        if st[0] == do_commands[0]:
            d[name] += int(st[2])
        else:
            d[name] -= int(st[2])
    if st[0] == 'BALANCE':
        if st[1] in d:
            res.append(d[st[1]])
        else:
            res.append('ERROR')
    if st[0] == 'TRANSFER':
        name1 = st[1]
        name2 = st[2]
        if name1 not in d:
            d[name1] = 0
        if name2 not in d:
            d[name2] = 0
        d[name1] -= int(st[3])
        d[name2] += int(st[3])
    if st[0] == 'INCOME':
        for name, sum in d.items():
            if sum > 0:
                d[name] *= (1 + int(st[1]) / 100)
for i in res:
    print(i)