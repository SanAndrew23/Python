from sys import stdin

lst = list(map(str, stdin.read().split()))
d = dict()
res = []
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
res = list(d.items())
res.sort(key=lambda x: x[1], reverse=True)
for i in res:
    print(f'{i[0]}', sep = '\n')