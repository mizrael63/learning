import random
ar = [random.randint(0, 100) for _ in range(15)]
print(ar)
dd = 0
while (all(ar[dd] < ar[dd + 1] for dd in range(len(ar) - 1))) == False:

    e = 0
    while e <= len(ar):
        for e in range(len(ar) - 1 - e):
            if ar[e] > ar[e + 1]:
                ar[e], ar[e + 1] = ar[e + 1], ar[e]
        e += 1
        break
        print(ar)
print(ar)