def R(N):
    a = bin(N)[2:]
    r = ""
    if N %2 == 0:
        r = "".join(list(map(str, a))) + ("0" * a.count("0"))
    else:
        r = ("1" * a.count("1")) + "".join(list(map(str, a)))
    
    return int(r, 2)


N = 1
while True:
    if R(N) > 2000:
        print(N)
        print(R(N))
        break
    N += 1