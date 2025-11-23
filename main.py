result = ''
for i in range(len(s := input())):
    if i % 3 != 0:
        result += s[i]
print(result)
