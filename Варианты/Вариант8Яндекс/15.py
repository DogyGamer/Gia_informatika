deli = lambda a,b: a % b == 0

def f(a,x):
    return not(deli(x, 3) and deli(x,5)) or (a >= (42-x))

for a in range(50):
    if all([f(a,x) for x in range(5000)]):
        print(a)
        