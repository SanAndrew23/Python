lst = [5, 98, 33, 1, 4, 7, 125]
# Сортирует список по возрастанию
lst.sort()
print(lst)

lst = [5, 98, 33, 1, 4, 7, 125]
# Сортирует список по убыванию
lst.sort(reverse=True)
print(lst)

lst = [5, 98, 33, 1, 4, 7, 125]
# Сортирует список по возрастанию суммы цифр
lst.sort(key=lambda x: sum(map(int, str(x))))
print(lst)

lst = ['xx', 'xxxxx', 'xxx', 'x', 'xxxxxx']
# Сортирует список по длине строки
lst.sort(key=len)
print(lst)

