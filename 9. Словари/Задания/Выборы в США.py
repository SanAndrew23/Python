d = dict()
count = int(input())
for i in range(count):
    a = input().split()
    if a[0] in d:
        d[a[0]] += int(a[1])
    else:
        d[a[0]] = int(a[1])

for key, word in d.items():
    print(f'{key} - {word}')
