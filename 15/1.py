sled = lambda a,b: 0 if a == 1 and b == 0 else 1

def razrsigma(a_,b_):
    a = list(map(int, bin(a_)[2:]))
    b = list(map(int, bin(b_)[2:]))
    if (len(a) > len(b)):
        b = [*[0]*(len(a)-len(b)),  *b]
    elif (len(b) > len(a)):
        a = [*[0]*(len(b)-len(a)), *a]

    c = []
    for i in range(len(a)):
        c.append(a[i] & b[i])

    return int("".join(list(map(str,c))), base=2)


F = lambda x,A: sled((razrsigma(x, 35) != 0) or (razrsigma(x, 22) != 0), sled( (razrsigma(x,15) == 0), razrsigma(x,A) != 0 ))

for A in range(100000):
    res = [F(x,A) for x in range(10000)]
    # print(res)
    if(all(res)):
        print("DONE!")
        print(A)
        