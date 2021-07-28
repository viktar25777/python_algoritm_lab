a = int(input("Введите число: "))
b = 0
for i in range(1, a + 1):
    b += i
    print(b)

a = 1
def func(a):
    try:
        a = int(input("Введите число: "))
    except zerodivisionerror:
        return
    s = a * (a + 1) // 2
    return s

print(b) == print(func(a))


