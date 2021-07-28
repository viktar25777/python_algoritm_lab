import random
from random import randint
randint(1, 100)
list = [randint(1, 100)]
n = 20
for i in range(n):
    list.append(int(randint(1, 100)))
    print('%3d' % list[i], end='')
    print()

if list[0] > list[1]:
    minimum_1 = 0
    minimum_2 = 1
else:
    minimum_1 = 1
    minimum_2 = 0

for i in range(2, n):
    if list[i] < list[minimum_1]:
        a = minimum_1
        minimum_1 = i
        if list[a] < list[minimum_2]:
            minimum_2 = a
        elif list[i] < list[minimum_2]:
            minimum_2 = i

print('№%3d:%3d' % (minimum_1 + 1, list[minimum_1]))
print('№%3d:%3d' % (minimum_2 + 1,
list[minimum_2]))

