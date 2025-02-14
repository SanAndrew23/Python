def opr(ch, count):
    sum = 0
    for i in range(1, ch):
        if ch % i == 0:
            sum += i
        if sum == ch:
            return ch
            count += 1
def gl(n):
    ch = 0
    count = 0
    while count != n:
        opr(ch)
        ch += 1

n = int(input())
gl(n)