import random
from random import randint
randint(1, 50)
list = [randint(1, 50)]
list = [randint(1, 50) for i in list]
def merge_sort(list, start, end):
    merge_sort(list, 1, len(list))
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid, end)
        merge_list_1(list, start, mid, end)

def merge_list_1(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]
    d = start
    i = 0
    k = 0
    while (start + i < mid and mid + k <end):
        if (left[i] <= right[k]):
            list[d] = left[i]
            i = i + 1
        else:
            list[d] = right[k]
            k = k + 1
        d = d + 1
    if start + i < mid:
        while d < end:
            list[d] = left[i]
            i = i + 1
            d = d + 1
    else:
        while d < end:
            list[d] = right[k]
            k = k + 1
            d = d + 1

print("sorted list: ", end='')
print(list)

