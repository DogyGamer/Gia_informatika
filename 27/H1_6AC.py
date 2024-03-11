lines = open("./27/H1_6_B.txt", "r").readlines()[1:]

upper_50 =  {x:0 for x in range(80)}
lower_50 = {x:0 for x in range(80)}

for a in lines:
    a = int(a)
    if a > 50:
        upper_50[a % 80] += 1
    else:
        lower_50[a % 80] += 1
    
suma = 0       
for i in range(1,40):
    if i != 0:
        j = 80-i
    else:
        j = 0
    
    suma += (upper_50[j]+lower_50[j])*upper_50[i] + upper_50[j]*lower_50[i]
    
    # print(i, j)
    
suma += lower_50[0]*upper_50[0] + upper_50[0]*(upper_50[0]-1)/2
suma += lower_50[40]*upper_50[40] + upper_50[40]*(upper_50[40]-1)/2
# a0[p]*a1[p] + a1[p]*(a1[p]−1)/2.
    
print(suma)

# Не понял как правильно считать кол-во пар, поэтому опирался на решение
