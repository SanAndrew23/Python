def sum_seq(a, b):
    if a == b:
        return b
    else:
        return a + sum_seq(a + 1, b)


print(sum_seq(1, 10))
