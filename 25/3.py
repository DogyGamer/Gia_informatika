# Рассмотрим произвольное натуральное число, представим его всеми возможными способами в виде произведения двух натуральных чисел и найдём для каждого такого произведения разность сомножителей. 
# Например, для числа 16 получим: 16  =  16*1  =  8*2  =  4*4, множество разностей содержит числа 15, 6 и 0. 
# Найдите все натуральные числа, принадлежащие отрезку [2 000 000; 3 000 000], у которых составленное описанным способом множество разностей будет содержать не меньше трёх элементов, не превышающих 115. 
# В ответе перечислите найденные числа в порядке возрастания.

for i in range(2000000, 3000000+1):
    k = 0
    for j in range(2, int(i**0.5)):
        if(i % j == 0):
            if(i//j - j) <= 115:
                k+=1
    
    if k > 2:
        print(i) 

print("end")