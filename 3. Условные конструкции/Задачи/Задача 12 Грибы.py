x = int(input())

pos = x % 10

if pos == 1:
    print('гриб')
elif 2 <= pos <= 4:
    print('гриба')
elif 5 <= pos <= 9 or pos == 0:
    print('грибов')