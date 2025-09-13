Case = '0123456789ABCDEFGHILKLMNOPQRSTUVWXYZ'
def translate(str):
    str = str [::-1]
    while str != 0:
        str[-1:-2]*16

str = input()