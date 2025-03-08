max = 0
posl = None
cur = 0

while True:
    a = int(input())
    if a == 0:
        break
    if posl is not None and a == posl:
        cur += 1
    else:
        cur = 1
    if cur > max:
        max = cur
    posl = a

print(max)
