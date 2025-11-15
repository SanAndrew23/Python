k, m, b = map(int, input().split())
count = int(input())
lst = []
for i in range(count):
    footballer = input().split()
    if k <= int(footballer[2]) <= m and int(footballer[3]) == b:
        lst.append(footballer)
for i in lst:
    print(*i[0:2])
print(len(lst))