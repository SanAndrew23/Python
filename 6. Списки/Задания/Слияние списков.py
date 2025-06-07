def merge(a, b):
    res = []
    a_1 = 0
    b_1 = 0
    while a_1 < len(a) and b_1 < len(b):
        if a[a_1] <= b[b_1]:
            res.append(a[a_1])
            a_1 += 1
        else:
            res.append(b[b_1])
            b_1 += 1
    res.extend(a[a_1:])
    res.extend(b[b_1:])
    return res


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(merge(a, b))
