def max_digit(num):
    max = 0
    while num != 0:
        ost = num % 10
        if ost > max:
            max = ost
        num //= 10
    return max


num = int(input())
print(max_digit(num))
