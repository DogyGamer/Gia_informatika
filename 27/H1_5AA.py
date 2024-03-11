lines = open("./27/H1_5_B.txt", "r").readlines()[1:]

max_osts = { k:0 for k in range(160)}
max_osts_7 = { k:0 for k in range(160)}

for a in lines:
    a = int(a)   
    if a % 7 == 0:
        max_osts_7[a % 160] = max(a, max_osts_7[a % 160] )
    else:
        max_osts[a % 160] = max(a, max_osts[a % 160] )
        
maxsum = 0
pair = [0,0]
for ost1 in range(160):
    for ost2 in range(160):
        
        if ost1 == ost2:
            continue
        
        a = max_osts_7[ost1]
        b = max(max_osts[ost2], max_osts_7[ost2])
        if a+b > maxsum:
            maxsum = a+b
            pair = [a,b]
            
print(*pair)
        
# Забыл как перебирать без повторений
# Было: 
# for ost1 in range(160):
#    for ost2 in range(ost1+1, 160):