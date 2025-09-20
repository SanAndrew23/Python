N = int(input())
M = int(input())
x = int(input())
y = int(input())

if N >= M:
    d1 = x
    d2 = N - x
    d3 = y
    d4 = M - y
else:
    d1 = y
    d2 = M - y
    d3 = x
    d4 = N - x

if d1 <= d2:
    min_l = d1
else:
    min_l = d2

if d3 <= d4:
    min_s = d3
else:
    min_s = d4

if min_l <= min_s:
    res = min_l
else:
    res = min_s

print(res)