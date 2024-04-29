lines = open("./Вариант3Яндекс/26.txt", "r").readlines()

stavki = {}

for line in lines:
    lotid, personid, stavka = list(map(int, line.split()))
    
    if lotid in stavki.keys():
        stavki[lotid].append(stavka)
    else:
        stavki[lotid] = [stavka]
        
cntr = 0
summa = 0    
for lotid, stav in stavki.items():
    if len(stav) >= 2:
        cntr += 1
        summa += sorted(stav)[-2]
        
print(cntr, summa)

# Тупо забыл что вторая сумма берется, какой ужас