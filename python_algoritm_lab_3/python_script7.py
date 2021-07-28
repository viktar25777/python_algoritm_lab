import numpy as np
n = 5
m = 4
def matrix(n, m):
    try:
        n = int(input("Введите число: "))
        m = int(input("Введите число: "))
        a = [55, 77, 88, 99]
        b = [77, 88, 99, 55]
        c = [55, 77, 88, 99]
        d = [55, 44, 77, 99]
    except zerodivisionerror:
        return
    f = n * m
    s = sum(a), sum(b), sum(c), sum(d)
    g = a, b, c, d, s
    f = g
    return f

print(matrix(n, m))


