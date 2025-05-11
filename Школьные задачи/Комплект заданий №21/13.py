s = input()[1::2]
res = ''
for i in range(len(s)):
    res += s[i].lower() if i % 2 == 0 else s[i].upper()
print(res)
