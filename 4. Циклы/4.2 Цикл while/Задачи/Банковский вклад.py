start_sum = float(input())
target_sum = float(input())
percent = float(input())

percent = percent / 12 / 100
a = 1

while start_sum <= target_sum:
    start_sum = start_sum + start_sum * percent
    print(f'{a} - {start_sum:.2f}')
    a += 1