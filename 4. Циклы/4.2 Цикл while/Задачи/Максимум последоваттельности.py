x = int(input())

max_num = x

while x != 0:
    x = int(input())
    if x > max_num:
        max_num = x

print(max_num)