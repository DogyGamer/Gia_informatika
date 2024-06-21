lines = open("./26.txt", "r").readlines()
S, W, N, K = list(map(int, lines[0].split()))
ys = list(map(lambda x: int(x.replace("\n", "")), lines[1:N+1]))
xs = list(map(lambda x: int(x.replace("\n", "")), lines[N+1:N+K+1]))

# print(ys)
# print(xs)

# pole = [[0]*S for _ in range(S)]

# for y in ys:
#     for yc in range(max(y-(W//2), 0), min(y+(W//2), S)):
#         for x in range(S):
#             pole[x][yc] += 1



# # print(len([x for x in pole[0] if x > 0]))

# for x in xs:
#     for xc in range(max(x-(W//2), 0), min(x+(W//2), S)):
#         for y in range(S):
#             pole[xc][y] += 1
# cntr = 0       
# for x in range(S):
#     for y in range(S):
#         if pole[x][y] > 0:
#             cntr += 1

def get_diap(arr):
    d = [] 
    for a in arr:  
        d.append([max(a-(W//2), 0), True])
        d.append([min(a+(W//2), S), False])

    cntr = 0
    diapazon_lol = []
    d = sorted(d)
    for t, isstart in d:
        if isstart:
            cntr += 1
            if cntr == 1:
                diapazon_lol.append([t,0])
        else:
            cntr -= 1
            if cntr == 0:
                diapazon_lol[-1][1] = t
    return diapazon_lol    


yd = get_diap(ys)
xd = get_diap(xs)

pl = 0
l = 0

for yst, ynd in yd:
    ly = ynd-yst
    l += ly
    pl += ly*S
    
for xst, xnd in xd:
    lx = xnd-xst
    pl += lx*S
    
for yst, ynd in yd:
    ly = ynd-yst
    for xst, xnd in xd:
        lx = xnd-xst
        pl -= lx*ly
        

print(l, pl)

