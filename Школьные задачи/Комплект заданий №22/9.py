amount = '123456789'
for i in input():
    if i.isdigit():
        amount.replace(i, '')
if amount != '':
    print(amount)
else:
    print('0')
