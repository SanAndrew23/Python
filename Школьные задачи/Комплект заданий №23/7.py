s = input().split()
negative_numbers = []
for i in s:
    if i[0] == '-' and i[1:].isdigit():
        negative_numbers.append(int(i))
print(str(max(negative_numbers)) if len(negative_numbers) > 0 else "NOOOO")
