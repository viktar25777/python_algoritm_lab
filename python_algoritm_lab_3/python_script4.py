import random
from random import randint
randint(1,
100)
list = []
n = 20
for i in range(n):
    list.append(int(randint(1, 100) - 50))
print(list)

i = 0
index = -1
while i < n:
    if list[i] < 0 and index == -1:
        index = i
    elif list[i] < 0 and list[i] > list[index]:
        index = i
    i += 1

print(index+1,':', list[index])

