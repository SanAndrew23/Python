def find_max(students):
    max_mark = 0
    for st in students:
        mark = int(st[3])
        if mark > max_mark:
            max_mark = mark
    return max_mark

f = open('Максимальный балл по классам.txt', encoding='utf-8')
students_9 = []
students_10 = []
students_11 = []
for line in f:
    st = line.split()
    if st[2] == '9':
        students_9.append(st)
    elif st[2] == '10':
        students_10.append(st)
    else:
        students_11.append(st)

print(find_max(students_9), find_max(students_10), find_max(students_11), sep=' ')
f.close()