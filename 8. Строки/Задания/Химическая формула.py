st = input()
pred_element = st[0]
f = True
lst1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZе'
lst2 = 'abcdefghijklmnopqrstuvwxyz'
if pred_element in lst2:
    f = False
cur_element = st[1]
if pred_element in lst2:
    f = False
if cur_element == pred_element:
    f = False
for i in st[1:]:
    if cur_element in lst1 or cur_element in lst2:
        cur_element = i
    else:
        pred_element = 'е'
    if pred_element == 'е':
        if cur_element not in lst1:
            f = False
    if cur_element == pred_element:
        f = False
    if pred_element in lst2 and cur_element in lst2:
        f = False
    pred_element = cur_element

if f:
    print('YES')
else:
    print('NO')