a = int(input("Введите число: "))
b = int(input("Введите число: "))
count = 0
for i in range(1, a + 1):
    n = int(input("Введите число " + str(i) + ": "))
    while n > 0:
        if n%10 == b:
            count += 1
        else:
            n = a // 10

print("Количество введённых %a чисел %a" % (count, a))
