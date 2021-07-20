a = 6
b = 6
c = 6
def treug(a, b, c):
    try:
        a = int(input("Введите число: "))
        b = int(input("Введите число: "))
        c = int(input("Введите число: "))
    except zerodivisionerror:
        return
    if a+b>c:
        print('Равнобедренный')
    else:
        print('Равносторонний')

print(treug(a, b, c))

