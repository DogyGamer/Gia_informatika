items = list(map(lambda x: int(x.replace("\n", "")), open("./17.txt", "r").readlines()))

min19 = min([x for x in items if x % 19 == 0])

msum = 0
cntr = 0

for i in range(len(items)-1):
    a = items[i]
    b = items[i+1]
    
    if a > min19 or b > min19:
        cntr += 1
        msum = max(msum, a+b)

print(cntr, msum)