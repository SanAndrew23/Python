count = int(input())
lst = list(map(int, input().split()))
k, m, d = map(int, input().split())

print(*(lst[0:k-1] + sorted(lst[k-1:m], reverse = d == -1) + lst[m:count]))