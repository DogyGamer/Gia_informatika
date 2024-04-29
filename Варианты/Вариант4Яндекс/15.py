sled = lambda a,b: 0 if a and not b else 1

def f(x, a):
    return (x&91 == 0) or sled((x&77 == 0), (x&a != 0))

for a in range(200):
    if all([f(x,a) for x in range(10000)]):
        print(a)