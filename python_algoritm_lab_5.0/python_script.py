a = dict(baza='name', kvartal='number')
b = []
g = 0
def sr(a, b):
    try:
        a = input("a = ")
        d = int(input("d = "))
        e = int(input("e = "))
        x = int(input("x = "))
    except valueerror and zerodivisionerror:
        return
    f = sum(range(e, x))
    g = f / d
    h = g / 2
    k = g / 1.5
    l = g / 2.5
    w = g * 2
    s = g, h, k, l, w
    return s

    if g>=0:
        print(f"{a}, Прибыль больше среднего")
    else:
        g<=0
        print(f"{a}, Прибыль меньше среднего")

print(f"{g>=0, a}, {g<=0, a}", sr(a, b))



