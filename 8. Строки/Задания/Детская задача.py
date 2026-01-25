string = '1'
count = 1
for i in range(s := int(input())):
    new_string = ''
    for j in range(len(string)):
        if j + 1 < len(string) and string[j] == string[j + 1]:
            count += 1
        else:
            new_string += (str(count) + string[j])
    print(string)
    string = new_string


print(string.split())