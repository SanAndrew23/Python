a, b  = map(int, input().split())
_a = abs(a)
_b = abs(b)

div = 0
while _a >= _b:
    _a -= _b
    div += 1

res = 0
if a >= 0 and b > 0:
    res = div
else:
    res = -div - 1

if a < 0 and b < 0:
    res = div + 1

print(res, a - res * b)