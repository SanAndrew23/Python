sum = 0.00
while (ch:=float(input())) != 0:
    if ch > 0:
        sum += ch - int(ch)
print(f'{sum:.2f}')