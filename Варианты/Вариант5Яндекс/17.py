arr = list(map(int, open("./17(4).txt", "r").readlines()))

m2 = min([x for x in arr if x > 0 and len(str(x)) == 2])

cntr = 0
mindiff = 999_999_999

for i in range(1,len(arr)):
    a = arr[i-1]
    b = arr[i]
    
    ac = not (str(m2) in str(a))
    bc = not (str(m2) in str(b))
    
    if ac or bc:
        cntr += 1
        mindiff = min(mindiff, abs(a-b))

print(cntr)
print(mindiff)
    
    