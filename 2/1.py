def sled(x,y):
    if(x == 1 and y == 0):
        return 0
    else:
        return 1
    
def ravenstvo(x,y):
    return x == y

def F(x,y,z,w):
    return (sled(x,y) == sled(z,w)) or (x and w)


print("x", "y", "z", "w")
for x1 in [0,1]:
    for y1 in [0,1]:
        for z1 in [0,1]:
            for w1 in [0,1]:
                res = F(x1,y1,z1,w1)
                if(res == 0):
                    print(x1,y1,z1,w1)