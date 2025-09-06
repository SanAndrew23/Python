x = int(input())
table = []
for i in range(x):
    name, num = input().split()
    table.append([name, num])

table.sort(key=lambda x: x[1], reverse=True)

for i in table:
    print(i[0])
