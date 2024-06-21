lines = list(map(lambda x: list(map(int, x.replace("\n", "").split())), open("./27_C.txt").readlines()))
N, K = lines[0]
lines = lines[1:]

optxz = -1
minzatr = 999_999_999

for xz in range(2,3):#N):
    zatr = 0
    cntr = 0
    dist = 0
    for s,e in lines:
        for p in range(s,e):
            road = min(abs(p - xz), abs((N-p)+xz))
            dist += road
            cntr += 1
    
    zatr = dist*(cntr*60)
    
    if zatr < minzatr:
        minzatr = zatr
        optxz = xz
        
print(minzatr, xz)
        
        