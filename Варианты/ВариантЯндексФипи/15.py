de = lambda a,b: a % b == 0

sled = lambda a,b: 0 if a and not b else 1

def f(x,a):
    return sled(((not de(x,a)) and de(x, 35)), ( (not de(x,21)) or (not de(x,35)) ))


for a in range(1, 301):
    if all([f(x,a) for x in range(1, 10000) ]):
        print(a)
