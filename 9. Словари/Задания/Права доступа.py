base = dict()
count1 = int(input())
file_commands = {'read': 'R', 'execute': 'X', 'write': 'W'}

for i in range(count1):
    parts = input().split()
    base[parts[0]] = parts[1:]

count2 = int(input())
result = []
for i in range(count2):
    parts = input().split()
    if file_commands[parts[0]] in base[parts[1]]:
        result.append('OK')
    else:
        result.append('Access denied')
for i in result:
    print(i, sep = '/n')