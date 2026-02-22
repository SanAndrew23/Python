lst = list(map(str, input().split()))
sp = ['flower;', 'gemstone;']
st = str([sp[i % 2] for i in range(len(lst))])
print(st[1:-2])