def is_palindrome(letters):
    c = 0
    for i in letters:
        if i % 2 != 0:
            c += 1
    return c <= 1

def generate_palindrome(letters):
    res = ''
    f = False
    x = ''
    for i in range(len(letters)):
        if letters[i] != 0:
            if letters[i] % 2 != 0:
                letters[i] -= 1
                x = chr(i + 65)
                f = True
            res += (letters[i] * (chr(i + 65)))
    if f:
        return res[::2] + x + (res[1::2])[::-1]
    else:
        return res[::2] + (res[1::2])[::-1]


s = input().upper()
letters = [0] * 28
count = 0
for i in s:
    letters[ord(i) - 65] += 1
if is_palindrome(letters):
    print(generate_palindrome(letters))