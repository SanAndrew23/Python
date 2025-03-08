def is_palindrome(number):
    old_number = number
    new_number = 0
    while number != 0:
        new_number = new_number * 10 + (number % 10)
        number //= 10
    return old_number == new_number


a, b = map(int, input().split())

for i in range(a, b + 1):
    if is_palindrome(i):
        print(i, end=' ')
