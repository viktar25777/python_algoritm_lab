a = 2
def away(a):
    try:
        a = int(input("Введите номер буквы латинского алфавита: "))
    except zerodivisionerror:
        return

    s = chr(a)
    return s

print(away(a))

