a = 2021
def year(a):
    try:
        a = int(input("Введите год числом: "))
    except zerodivisionerror:
        return
    b = a // 4
    c = a // 400
    d = a // 100 != 0
    s = a // b and c // d
    return s

print(year(a))




