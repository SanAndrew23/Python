def translate(num, system):
    string = ''
    while num != 0:
        string += str(num%system)
        num //= system
    print(string)


num, system = map(int, input().split())
translate(num, system)