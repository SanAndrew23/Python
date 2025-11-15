s = input()
k = int(input())
while len(s) >= k:
    print(s[::-k])
    print(s[::k])
    s = s[1::-k] + s[1::k]