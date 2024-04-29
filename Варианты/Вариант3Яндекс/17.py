lines = open("./Вариант3Яндекс/17.txt", "r").readlines()

cntr = 0
msum = 0

mcc = max([int(line) for line in lines if len(line.replace("\n", "")) == 3])**3

for i in range(len(lines)-1):
    a2 = int(lines[i])
    b2= int(lines[i+1])
    
    a = sum(list(map(int, str(a2).replace("-", ""))))
    b = sum(list(map(int, str(b2).replace("-", ""))))
    
    modrazn = abs(a2**2 - b2**2)
    
    if not ((a % 5 == 0) ^ (b % 5 == 0)):
        continue
    
    if modrazn >= mcc:
        cntr += 1
        msum = max(msum, a2+b2)
    
print(cntr, msum)

# .replace("\n", "")
# Обалдеть блин. Правильный ответ получился добавлением этого куска в 6ю строку...