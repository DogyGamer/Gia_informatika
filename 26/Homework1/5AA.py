lines = list(map(int, open("./26/Homework1/26_5.txt", "r").readlines()))[1:]

lines.sort()

def binsearch(arr, elem):
    l = 0
    r = len(arr)
    while r-l > 1:
        m = (l+r) // 2
        if arr[m] > elem:
            r = m
        else:
            l = m
    return arr[l] == elem 

counter = 0
lmax = 0
for a in range(len(lines)-1):
    for b in range(a+1, len(lines)):
        if(lines[a]%2 == 0 and lines[b] % 2 == 0):
            avg = ( (lines[a]+lines[b]) // 2)
            if binsearch(lines, avg):
                counter += 1
                lmax = max(lmax, avg)
            
print(counter, lmax)
# 15 976339247

# Long answer
# 