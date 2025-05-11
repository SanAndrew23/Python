def max_digit(num, maximus):
    if num == 0:
        return maximus
    else:
        if num % 10 > maximus:
            maximus = num % 10
        return max_digit(num // 10, maximus)


num = int(input())
print(max_digit(num, 0))
