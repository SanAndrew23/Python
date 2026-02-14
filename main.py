res = []
for i in range(int(input())):
    res.append(input())
for i in range(len(res)):
    if i % 2 != 0:
        del(i)
print(res)