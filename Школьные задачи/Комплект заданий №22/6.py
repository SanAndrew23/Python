count = 0
amount = 0
current_number = 0
for part in input():
    if part.isdigit():
        current_number = current_number * 10 + int(part)
    else:
        if current_number % 10 == 0 and 99 < current_number < 1000:
            amount += current_number
            count += 1
        current_number = 0
if current_number % 10 == 0 and 99 < current_number < 1000:
    amount += current_number
    count += 1
print(f'{amount / count:.2f}')
