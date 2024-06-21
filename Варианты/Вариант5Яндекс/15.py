
deli = lambda n,m: n % m == 0

f = lambda a,x: (not deli(x, 72)) or deli(x, 495) or (not deli(x, a))


for a in range(1, 1000):
    res = [f(a,x) == 1 for x in range(1, 1_000_000)]
    if all(res):
        print(a)