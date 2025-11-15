list = []
while (surname := input()) != '':
    list.append(surname)
list.sort(key = lambda x: x.split()[1])
for i in range(1, len(list) + 1):
    print(f'{i}. {list[i-1]}')