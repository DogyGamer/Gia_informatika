lines = open("./27/H1_10_A.txt", "r").readlines()[1:]

osts = {k:[0,0,0] for k in range(3)}
osts2 = {k:[0] for k in range(3)}

for a in lines:
    a = int(a)
    
    if a % 3 == 0:
        if a >= osts[0][0]:
            osts[0][2] = osts[0][1]
            osts[0][1] = osts[0][0]
            osts[0][0] = a
        elif a >= osts[0][1]:
            osts[0][2] = osts[0][1]
            osts[0][1] = a
        elif a >= osts[0][2]:
            osts[0][2] = a
    elif a % 3 == 1:
        if a >= osts[1][0]:
            osts[1][2] = osts[1][1]
            osts[1][1] = osts[1][0]
            osts[1][0] = a
        elif a >= osts[1][1]:
            osts[1][2] = osts[1][1]
            osts[1][1] = a
        elif a >= osts[1][2]:
            osts[1][2] = a
    elif a % 3 == 2:
        if a >= osts[2][0]:
            osts[2][2] = osts[2][1]
            osts[2][1] = osts[2][0]
            osts[2][0] = a
        elif a >= osts[2][1]:
            osts[2][2] = osts[2][1]
            osts[2][1] = a
        elif a >= osts[2][2]:
            osts[2][2] = a


for a in lines:
    a = int(a)
    osts2[a%3].append(a)

# print(sorted(osts2[0]))
# print(sorted(osts2[1]))
# print(sorted(osts2[2]))

    
print(max( sum(osts[0]), sum(osts[1]), sum(osts[2]), osts[0][0]+osts[1][0]+osts[2][0]  ))



# File A - Wrong Answ
# File B - Correct Answ 

# Why?
# https://i.pinimg.com/474x/70/30/70/7030703e5c4542397ab6cc854bfe33e5.jpg
