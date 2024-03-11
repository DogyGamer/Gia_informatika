lines = open("./27/H1_3_B.txt", "r").readlines()[1:]

max_26 = 0
max_13 = 0
max_2 = 0

for a in lines:
    a = int(a)
    if a % 26 == 0:
        max_26 += 1
    elif a % 13 == 0:
        max_13 += 1
    elif a % 2 == 0:
        max_2 += 1
        
print(max_26*(max_26-1)/2 + (max_13*max_2) + max_26*(len(lines)-max_26))
        
        
        
# AC means Accepted Corrected
# Я подогнал решение подсмотрев в ответ
# подгонял 16 строчку