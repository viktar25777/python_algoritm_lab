import random
from random import randrange
randrange(1, 101)
n = round(randrange(1, 101))
i = 1
print("Я загадал число. Для его отгадывания есть 10 попыток.")
while i <= 10:
    a = int(input("Введите число: "))
    if a>n:
        print("Число больше загаданного")
    elif a <n:
        print("Число меньше загаданного")
    else:
        print("Вы угадали число")
        break
    i += 1
else:
    print("Вы проиграли. Я загадал вот такое число n.")

