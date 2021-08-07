import random
from random import randint
randint(1, 150)
n = 20
list = [randint(1, 150)]
for i in range(n):
    list = int(randint(1, 150))
    print('%3d' % list, end='')
    print()

list_minimum = 0
list_maximum = 0
for i in range(1, n + 1):
    if list < list_minimum:
        list_minimum = list
    elif list > list_maximum:
        list_maximum = list
print(list_minimum, list_maximum)

if list_minimum > list_maximum:
    list_minimum, list_maximum = list_maximum, list_minimum

sum = 0
for i in range(list_minimum + 1, list_maximum):
    sum += list

print(sum)
