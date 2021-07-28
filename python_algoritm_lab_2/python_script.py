a = 50
b = '+', '-', '*', '/', '0'
c = 75
def func(a, b, c):
    try:
        a = int(input("Введите число: "))
        b = input("Введите математический знак действия: ")
        c = int(input("Введите число: "))
    except zerodivisionerror:
        return
    if b==0:
        print("Программа завершила свою работу")
    elif c==0:
        print("Делить на ноль нельзя")
    else:
        a = int(input("Введите число: "))
        b = input("Введите математический знак действия: ")
        c = int(input("Введите число: "))
    d = a + c
    e = a - c
    f = a * c
    g = a / c
    print(d, e, f, g)

print(func(a, b, c))
