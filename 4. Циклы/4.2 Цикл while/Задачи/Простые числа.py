x = int(input())

count = 0
ch = 1
while not(x == count):
    for i in range(2,  x):
        if x % i != 0:
            count += 1
            print(ch, end = ' ')
            ch += ch