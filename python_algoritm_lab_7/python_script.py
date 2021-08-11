import random
from random import randint
randint(-100, 100)
n = randint(-100, 100)
mas = [randint(-100, 100) for i in range(n)]
for i in range(n):
    print(mas[i], sep='')
print('   ')
for i in range(n - 1):
    for k in range(n - 2, i - 1, -1):
        if mas[k] < mas[k+1]:
            mas[k], mas[k+1] = mas[k+1], mas[k]
for i in range(n):
    print(mas[i], sep='')
print('   ')

