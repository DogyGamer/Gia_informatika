from itertools import product

cntr = 0

res = []

for word in product("БАНДЕРОЛЬ", repeat=7):
    if word.count("Ь") > 1:
        continue

    
    w2 = "".join(word).replace("Б", "!").replace("Н", "!").replace("Д", "!").replace("Р", "!").replace("Л", "!")
    if "Е!" in w2 or "!Е" in w2:
        continue
    
    cntr += 1
    # print(w2)
    res.append("".join(word))
    
print(cntr)
print(len(set(res)))