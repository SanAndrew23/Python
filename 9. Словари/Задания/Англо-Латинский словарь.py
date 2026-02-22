d = dict()
res = []
for i in range(int(input())):
    st = input().split('-')
    word = st[0]
    syn = []
    synonims = ''
    for j in st[1]:
        syn.append(j)
    for i in syn:
        if i != ',':
            synonims += i
    for i in synonims.split():
        d[i] = word
for i in range(int(input())):
    a = input()
    res.append(f'{a} - {d[a]}')

for i in res:
    print(i)