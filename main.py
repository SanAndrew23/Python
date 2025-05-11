s = set()
def f(x, count):
    if count == 4:
        s.add(x)
        return 1
    return f(x * 2, count + 1) + f(x / 2, count + 1) + f(x * 3, count +1)

print(f(2560, 0))
print(s)
print(len(s))
