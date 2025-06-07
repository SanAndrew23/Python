lst = list(map(int, input().split()))
max_pos = 0
min_pos = 0
for i in range(len(lst)):
    if lst[i] > lst[max_pos]:
        max_pos = i
    if lst[i] < lst[min_pos]:
        min_pos = i
lst[min_pos], lst[max_pos] = lst[max_pos], lst[min_pos]
print(lst)