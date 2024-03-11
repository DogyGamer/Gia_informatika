lines = open("./26/Homework1/26_4.txt", "r").readlines()
N, M = map(int, lines[0].split())

def prep(x):
    a = x.split()
    return int(a[0]), int(a[1]), a[2]

lines = [prep(x) for x in lines[1:]]

B = [x for x in lines if x[2] == "B"]
A = [x for x in lines if x[2] == "A"]

A_sum = sum([x[0]*x[1] for x in A]) #Считаем стоимость всех товаров А
ost = M-A_sum #Выводим остаток бюджета на товары B
B.sort(key=lambda x: x[0])
B_summ = [x[0]*x[1] for x in B]

last_ind = 0
for i in range(len(B_summ)):
    if sum(B_summ[:i]) > ost:
        last_ind = i-1
        break
    
gatheredB = sum([x[1] for x in B][:last_ind])
ost2 = ost - sum(B_summ[:last_ind])

colvo = 0
for i in range(1, B[last_ind][1]+1):
    ost3 = ost2 - B[last_ind][0]*i
    if ost3 < 0:
        colvo = i-1
        break
        
print(gatheredB+colvo, ost2 - B[last_ind][0]*colvo)