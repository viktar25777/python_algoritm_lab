a = 'b'
b = 'd'
def away(a, b):
    try:
        a = input("Введите строчную букву латинского алфавита: ")
        b = input("Введите строчную букву латинского алфавита: ")
    except valueerror and zerodivisionerror:
        return
    c = ord(a) - 97 + 1
    d = ord(b) - 97 + 1
    f = ord(b) - ord(a)
    return c, d, f

print(away(a, b))

