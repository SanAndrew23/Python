def is_perfect(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number


def main(n):
    number = 1
    count = 0
    while count != n:
        if is_perfect(number):
            count += 1
            print(number, end=' ')
        number += 1


n = int(input())
main(n)
