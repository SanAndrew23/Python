def shift_right(lst, count):
    return lst[-count:] + lst[:-count]


def shift_left(lst, count):
    return lst[count:] + lst[:count]


lst = list(map(int, input().split()))
count = int(input())
print(shift_right(lst, count))
