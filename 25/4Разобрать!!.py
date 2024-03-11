# Найдите все натуральные числа, принадлежащие отрезку [45 000 000; 50 000 000], у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым). В ответе перечислите найденные числа в порядке возрастания.

# for i in range(45000000, 50000000+1):
#     cnt = 0
#     deliteli = []
#     for j in range(1, int(i**0.5)):
#         if i % j == 0:
#             if j % 2 != 0:
#                 deliteli.append(j)


#     if len(set(deliteli)) == 5:
#         print(i)

#     cnt = 0

def kd(p):
    a = []
    z = 1
    while p % 2 == 0:
        p = p//2
    if (p ** 0.25) == int(p ** 0.25):
        for i in range(2,int(p**0.5)+1):
            if p % i == 0:
                if i % 2 == 1:
                    a.append(i)
                    if (p//i) % 2 == 1:
                        a.append(p//i)
                if len(a) >= 4:
                    break
        z = len(set(a)) + 1
        if p % 2 == 1:
            z += 1
    return z
for i in range(45000000,50000001):
    if kd(i) == 5:
        print(i)