import random
from random import randint
m, n, y, z= [int(input(i ))for i in ("n = ","m = ","y = ","z = ")]
matrix = [[randint(y, z) for _ in range (n)]for k in range (m)]
print(matrix)
for i in matrix:
    print(*i)

for x in range(m):
    print(min(matrix[x]))

a = min(matrix[x])
print(a)



