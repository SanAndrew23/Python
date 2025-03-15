def to_bin(n, b):
    if n != 0:
        to_bin(n // b)
        print(n % b, end='')

to_bin(10, 3)