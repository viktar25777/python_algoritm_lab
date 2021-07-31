import math
from math import sqrt
n = int(input("n = "))
k = int(input("k = "))
list = [2]
for i in range(2, n + 1):
    if i > 10:
        if (i%2 == 0) or (i%10 == 5):
            continue
    for k in list:
        if k >int((sqrt(i)) + 1):
            list.append(i)
            break
        if i%k == 0:
            break
        else:
            list.append(i)
            print(list)


