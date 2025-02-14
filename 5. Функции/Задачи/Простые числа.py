def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

x = int(input())

count = 0
number = 1
while count < x:
    if is_prime(number):
        print(number, end=' ')
        count += 1
    number += 1