a = [0] * 8
for i in range(2, 100):
    for k in range(2, 10):
        if i%k == 0:
            a[k-2] += 1
            i = 0
while i < len(a):
    print(i + 2, ' - ', a[i])
    i += 1

