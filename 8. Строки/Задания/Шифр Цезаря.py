def encode(st, key):
    st2 = ''
    for i in st:
        st2 += str(chr((ord(i) + key - 65) % 26 + 65))
    return st2

def decode(st, key):
    st2 = ''
    for i in st:
        st2 += str(chr((ord(i) - key - 65) % 26 + 65))
    return st2

st = input()
key = int(input())
print(encode(st, key))
print(decode(st, key))
