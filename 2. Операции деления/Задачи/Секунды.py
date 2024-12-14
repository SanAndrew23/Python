ch = int(input())

h = ch // 3600
min = ch % 3600 // 60
s = ch % 60

print("{}:{}:{}".format(h, min, s))