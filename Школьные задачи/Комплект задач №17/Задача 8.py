num = int(input())
sum = 0
f = True
if num < 0:
    num = abs(num)
    f = False
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        f = False
if f:
    print('YES', end=' ')
else:
    print('NO', end=' ')

count = 0
max_digit = 0
i = 1
place = 0
while num != 0:
    sum += num % 10
    count += 1
    if num % 10 > max_digit:
        max_digit = num % 10
        place = i
    i += 1
    num //= 10
print(sum, count, max_digit, i - place, end=' ')

