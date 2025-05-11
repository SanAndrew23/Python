amount = 0
digits = '13579'
for part in input():
    if part in digits:
        amount += int(part)
print(amount)