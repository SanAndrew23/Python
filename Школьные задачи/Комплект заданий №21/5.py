line = input()
index = line.find('f')
if index == -1:
    print(-2)
else:
    print(line.find('f', index + 1))
