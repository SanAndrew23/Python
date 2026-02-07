def try_s(ch):
    x1 = ch % 10
    x2 = ch // 10 % 10
    x3 = ch // 100
    if 99 < x1 * x2 * x3 < 1000:
        return True

n = int(input())
ch = 268
st = []
for i in range(n):
    st.append('')
for i in range(n):
    while try_s(ch) != True:
        ch += 1
    st[i] = ch
    ch += 1
print(*st)