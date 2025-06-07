lst = list(map(int, input().split()))
lst.sort(key=lambda x: x == 0)
print(lst)
