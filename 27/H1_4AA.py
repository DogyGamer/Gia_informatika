lines = open("./27/H1_4_B.txt", "r").readlines()[1:]

    
nechet_max = 0
nechet_max_7 = 0
nechet_max_7_2 = 0


chet_max = 0
chet_max_7 = 0
chet_max_7_2 = 0

for a in lines:
    a = int(a)
    if a % 2 == 0:
        if a % 17 == 0:
            if a >= chet_max_7:
                chet_max_7_2 = chet_max_7
                chet_max_7 = a
        else:
            chet_max = max(chet_max, a)
    else:
        if a % 17 == 0:
            if a >= nechet_max_7:
                nechet_max_7_2 = nechet_max_7
                nechet_max_7 = a
        else:
            nechet_max = max(nechet_max, a)

a1 = max(nechet_max, nechet_max_7_2)
b1 = nechet_max_7

a2 = max(chet_max, chet_max_7_2)
b2 = chet_max_7

if a1+b1 > a2+b2:
    print(a1,b1)
else:
    print(a2, b2)
