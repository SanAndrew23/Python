x = int(input())

pos2 = x % 100
pos = x % 10

if 11 <= pos2 <= 19:
    print('грибов')
elif 2 <= pos <= 4:
    print('гриба')
elif pos == 1:
    print('гриб')
else:
    print('грибов')