d = dict()
for i in range(int(input())):
    a = input().split()
    d[a[0]] = a[1]
    d[a[1]] = a[0]
key = input()
print(d[key])