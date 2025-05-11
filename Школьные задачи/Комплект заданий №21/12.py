words = input().split()
letters = input()
f = True
for word in words:
    for ch in word:
        if ch not in letters:
            f = False
            break
if f:
    print(*words, sep='\n')
else:
    print('NO')
