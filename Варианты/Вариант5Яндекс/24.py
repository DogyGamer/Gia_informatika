text = open("./24(4).txt", "r").readlines()[0].replace("\n","")

first_t = 0
first_u = 0

maxlen = 0

for i in range(1,len(text)):
    start = min(first_t, first_u)
    cntT = text[start:i+1].count("T")
    cntU = text[start:i+1].count("U")
    
    if cntT >= 100 and cntU >=50:
        first_t = max(first_t, first_u)+1
        first_u = first_t
    elif cntT >= 100:
        first_t += 1
        if first_u <= first_t:
            first_u = first_t
    elif cntU >= 50:
        first_u += 1
        if first_t <= first_u:
            first_t = first_u
        
    start2 = min(first_u, first_t)
    
    maxlen = max(maxlen, len(text[start2:i+1]))
    
print(maxlen)