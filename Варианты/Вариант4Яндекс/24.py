chrs = [chr(x) for x in range(65,91)]

stroka = open("./24(3).txt", "r").readlines()[0]

for cha in chrs:
    stroka = stroka.replace(cha, " ")
    
arr = list(map(int, stroka.split()))
print(max(arr))