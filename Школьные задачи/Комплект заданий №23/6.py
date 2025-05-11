f1 = False
f2 = False
f3 = False
f4 = False
qwerty = 'qwertyuiopasdfghjklzxcvbnm'
for i in (x:=input()):
    if i in qwerty:
        f1 = True
    if i in qwerty.upper():
        f2 = True
    if i.isdigit():
        f3 = True
if len(x) >= 8:
    f4 = True
if f1 and f2 and f3 and f4:
    print('YES')
else:
    print('NO')
