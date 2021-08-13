a = int(input("Введите число: "))
max_c = 0
max_b = 0
b = 758
def func(b):
    try:
        b = int(input("Введите число: "))
    except zerodivisionerror:
        return
    d = b //100
    s = d + d + d
    return s

print(func(b))

