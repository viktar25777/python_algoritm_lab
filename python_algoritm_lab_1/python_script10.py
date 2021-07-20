a = 205
b = 175
c = 985
def sravn(a, b, c):
    try:
        a = int(input("Введите число: "))
        b = int(input("Введите число: "))
        c = int(input("Введите число: "))
    except zerodivisionerror:
        return
    d = a > b or a < b
    e = a > c or a < c
    f = b > c or b < c
    g = c > a or c < a
    h = c > b or c < b
    if a>b>c:
        print(a)
    if b>a>c:
        print(b)
    if c>b>a:
        print(c)
    return d, e, f, g, h

print(sravn(a, b, c))

