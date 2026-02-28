f = open('Задание 1001.txt', encoding='utf-8')
ch = 0
res = 0
while c := f.read(1):
    if c.isdigit():
        ch = ch * 10 + int(c)
    else:
        res += ch
        ch = 0
print(res)
f.close()