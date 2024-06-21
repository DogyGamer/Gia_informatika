arr = list(map(int, open("17(8).txt").readlines()))

min35 = min([x for x in arr if len(str(x))== 3 and str(x)[-1] == "5"])


cntr = 0
msm = 0

for i in range(len(arr)-1):
    pair = arr[i:i+2]
    s = sum(pair)
    # if not any([len(str(x)) == 3 for x in pair]):
    #     continue

    
    if s % min35 == 0 and (len(str(pair[0])) == 3 or len(str(pair[1])) == 3):
        cntr += 1
        msm = max(msm, s)
        
print(cntr, msm)