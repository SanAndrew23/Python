x = int(input())

for i in range(x):
    for j in range(x, i, -1):
        print(j, end ='')
    print()