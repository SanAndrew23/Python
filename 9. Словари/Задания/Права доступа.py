base = dict()
count1 = int(input())
file_comands = {'read': 'R', 'execute': 'X', 'write': 'W'}

for i in range(count1):
    st = input()
    file = st[:st.find(' ')]
    comands = st[st.find(' ') + 1:]
    base[file] = comands

count2 = int(input())
result = []
for i in range(count2):
    st1 = input()
    if file_comands[st1[:st1.find(' ')]] in base[st1[st1.find(' ') + 1:]]:
        result.append('OK')
    else:
        result.append('Access denied')
for i in result:
    print(i, sep = '/n')