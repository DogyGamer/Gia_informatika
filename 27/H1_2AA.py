lines = open("./27/H1_2_B.txt", "r").readlines()[1:]

max_2 = 0
max_7 = 0
max_14 = 0
max_any = 0

for a in lines:
    a = int(a)
    if a % 14 == 0 and a > max_14:
        max_14 = a
        continue
    elif a % 7 == 0 and a > max_7:
        max_7 = a
        continue
    elif a % 2 == 0 and a > max_2:
        max_2 = a
        continue
    else:
        max_any = max(max_any, a)
    
print(max(max_2*max_7, max_14*max_any))

            