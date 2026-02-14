d = dict()
res = []
for i in range(int(input())):
    st = input().split('-')
    word = st[0]
    syn = []
    for i in st[1]:
        syn.append(i)
    for i in syn:
        d[word] = i
for i in range(int(input())):
    a = input()
    res.append(d[a])

for i in res:
    print(i)