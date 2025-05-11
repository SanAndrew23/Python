amount = 0
current_number = 0
for part in input():
    if part.isdigit():
        current_number = current_number * 10 + int(part)
    else:
        amount += current_number
        current_number = 0
print(amount + current_number)