lst = list(map(int, input().split()))
x = int(input())
count = 0
for i in lst:
    count += 1
    if x > i:
        break
print(count)