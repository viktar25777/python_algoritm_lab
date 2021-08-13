a = []
for i in range(10):
    a.append(int(input("Введите число: ")))

maximum = max(a)
minimum = min(a)
for i in range(len(a)):
    if i==maximum:
        a = minimum
    elif i==minimum:
        a = maximum

b = maximum =max(a)
c = minimum = min(a)
d = b, c = c, b
print(d)
print(a)


