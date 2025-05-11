amount = 0
for part in input().split():
    if part.isnumeric():
        amount += int(part)
print(amount)