import random
from random import randint
randint(1, 151)
list = [randint(1, 151) for i in range(randint(1, 151))]
def list_sort(list):
    for i in range(randint(1, 151)):
        n = len(list)
        if n % 2 == 0:
            median1 = list[n // 2]
            median2 = list[n // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = list[n // 2]
    s = sorted(list)
    return s[n // 2 + 1]

print(list_sort(list))


