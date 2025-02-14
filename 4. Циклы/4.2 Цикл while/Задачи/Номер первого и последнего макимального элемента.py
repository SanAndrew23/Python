a = int(input())

count = 1
first_index = 0
last_index = 0
maxim = a

while a != 0:
    a = int(input())
    if a > maxim:
        first_index = count
        maxim = a
    if a == maxim:
        last_index = count
    count += 1
print(first_index, last_index)