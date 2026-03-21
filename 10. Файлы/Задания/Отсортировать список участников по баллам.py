from sys import stdin

competitors = []
for line in stdin:
    last_name, first_name, _, mark = line.split()
    competitors.append((last_name, first_name, int(mark)))

for i in sorted(competitors, key=lambda x: (-int(x[3]), x[0], x[1])):
    print(i[0], i[1], i[2])