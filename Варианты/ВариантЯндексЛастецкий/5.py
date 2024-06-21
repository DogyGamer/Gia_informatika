inv = lambda x: "0" if x == "1" else "1"

def R(n):
    n2 = list(bin(n)[2:])
    if n2[-1] == n2[-2]:
        n2.insert(-1, inv(n2[-1]))
    else:
        n2[-1] = inv(n2[-1])
        n2[-2] = inv(n2[-1])
        n2.append(n2[-1])
        
    return int("".join(n2), 2)


for n in range(2, 100):
    r = R(R(n))
    if r > 168:
        print(n, r)