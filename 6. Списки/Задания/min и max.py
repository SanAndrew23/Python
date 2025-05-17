import sys

lst = list(map(int, input().split()))
max = -sys.maxsize
min = sys.maxsize
count = 0
for i in lst:
    count += 1
    if i > max:
        max = i
        place_max = count
    if i < min:
        min = i
        place_min = count
del lst[place_max]
del lst[place_min]