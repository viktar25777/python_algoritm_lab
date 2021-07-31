n = int(input("Введите число максимума: "))
sieve = set(range(2, n + 1))
while sieve:
    prine = min(sieve)
    print(prine, end='')
    sieve -= set(range(prine, n + 1, prine))

